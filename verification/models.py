# from django.db import models
# import qrcode
# from io import BytesIO
# from django.core.files import File
# import random
# import string

# class DrugBatch(models.Model):
#     batch_number = models.AutoField(primary_key=True)
#     drug_name = models.CharField(max_length=100)
#     manufacturer =models.CharField(max_length=100)
#     production_date =models.DateField()
#     expiry_date =models.DateField()
#     serial_number =models.CharField(max_length=100,unique=True,blank=True)
#     qr_code_img = models.ImageField(upload_to='qr_codes/',blank=True)

#     def __str__(self):
#         return f"{self.drug_name} - Batch {self.batch_number}"
    
#     def save(self,*args,**kwargs):
#         if not self.serial_number:
#             self.serial_number=self.generate_serial_number()


#         # Step 2: if object is new, save first to get batch_number
#         if not self.pk:
#             super().save(*args, **kwargs)

#         qr_data = f" Batch : { self.batch_number}\nSerial:{self.serial_number}"
#         qr =  qrcode.make(qr_data)
#         canvas = BytesIO()
#         qr.save(canvas,format='PNG')
#         filename =f'qr_code_{self.serial_number}.png'
#         self.qr_code_img.save(filename,File(canvas),save=False)
#         canvas.close()

#         super().save(*args,**kwargs)
    
#     def generate_serial_number(self):
#         return ''.join(random.choices(string.ascii_uppercase +string.digits , k=12))

from django.db import models
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile  # Safe for Django ImageField
import random
import string
import tempfile
import os
from .utils import upload_qr_to_supabase  # ✅ Add this import

class DrugBatch(models.Model):
    batch_number = models.AutoField(primary_key=True)
    drug_name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    production_date = models.DateField()
    expiry_date = models.DateField()
    serial_number = models.CharField(max_length=100, unique=True, blank=True)
    qr_code_img = models.ImageField(upload_to='qr_codes/', blank=True)
    qr_code_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.drug_name} - Batch {self.batch_number}"

    def save(self, *args, **kwargs):
        # 1️⃣ Serial generate karo agar blank ho
        if not self.serial_number:
            self.serial_number = self.generate_serial_number()

        # 2️⃣ Save once to get PK if new
        if not self.pk:
            super().save(*args, **kwargs)

        # 3️⃣ QR code bana
        qr_data = f"Batch: {self.batch_number}\nSerial: {self.serial_number}"
        qr = qrcode.make(qr_data)
        canvas = BytesIO()
        qr.save(canvas, format='PNG')
        canvas.seek(0)

        filename = f'qr_code_{self.serial_number}.png'

        # 4️⃣ Local ImageField mein save karo
        self.qr_code_img.save(filename, ContentFile(canvas.read()), save=False)

        # 5️⃣ Supabase upload — safe temp file use karo
        canvas.seek(0)  # Reset pointer
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
            tmp_file.write(canvas.getvalue())
            tmp_file.flush()
            tmp_file.close()  # Windows permission error avoid

            # Call Version B util
            self.qr_code_url = upload_qr_to_supabase(filename, tmp_file.name)

        canvas.close()
        # canvas.seek(0)
        # with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
        #     tmp_file.write(canvas.getvalue())
        #     tmp_file.flush()
        #     tmp_file.close()  # Windows safe

        #     # Safe Supabase remove + upload
        #     self.qr_code_url = upload_qr_to_supabase(filename, tmp_file.name)

        #     # Optional cleanup local temp
        #     os.remove(tmp_file.name)    # duplicate error rakham krna ka liya

        # canvas.close()


        # 6️⃣ Final DB save
        super().save(*args, **kwargs)

    def generate_serial_number(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
