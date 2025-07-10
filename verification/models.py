# # from django.db import models
# # import qrcode
# # from io import BytesIO
# # from django.core.files import File
# # import random
# # import string

# # class DrugBatch(models.Model):
# #     batch_number = models.AutoField(primary_key=True)
# #     drug_name = models.CharField(max_length=100)
# #     manufacturer =models.CharField(max_length=100)
# #     production_date =models.DateField()
# #     expiry_date =models.DateField()
# #     serial_number =models.CharField(max_length=100,unique=True,blank=True)
# #     qr_code_img = models.ImageField(upload_to='qr_codes/',blank=True)

# #     def __str__(self):
# #         return f"{self.drug_name} - Batch {self.batch_number}"
    
# #     def save(self,*args,**kwargs):
# #         if not self.serial_number:
# #             self.serial_number=self.generate_serial_number()


# #         # Step 2: if object is new, save first to get batch_number
# #         if not self.pk:
# #             super().save(*args, **kwargs)

# #         qr_data = f" Batch : { self.batch_number}\nSerial:{self.serial_number}"
# #         qr =  qrcode.make(qr_data)
# #         canvas = BytesIO()
# #         qr.save(canvas,format='PNG')
# #         filename =f'qr_code_{self.serial_number}.png'
# #         self.qr_code_img.save(filename,File(canvas),save=False)
# #         canvas.close()

# #         super().save(*args,**kwargs)
    
# #     def generate_serial_number(self):
# #         return ''.join(random.choices(string.ascii_uppercase +string.digits , k=12))

# from django.db import models
# import qrcode
# from io import BytesIO
# from django.core.files import File
# import random
# import string

# class DrugBatch(models.Model):
#     batch_number = models.AutoField(primary_key=True)
#     drug_name = models.CharField(max_length=100)
#     manufacturer = models.CharField(max_length=100)
#     production_date = models.DateField()
#     expiry_date = models.DateField()
#     serial_number = models.CharField(max_length=100, unique=True, blank=True)
#     qr_code_img = models.ImageField(upload_to='qr_codes/', blank=True)

#     def __str__(self):
#         return f"{self.drug_name} - Batch {self.batch_number}"

#     def save(self, *args, **kwargs):
#         # ✅ Step 1: Serial Number agar nahi hai toh generate karo
#         if not self.serial_number:
#             self.serial_number = self.generate_serial_number()

#         # ✅ Step 2: Agar new object hai (pk nahi mili) toh pehle ek baar save karo
#         if not self.pk:
#             super().save(*args, **kwargs)

#         # ✅ Step 3: Agar QR code already nahi hai tabhi generate karo
#         if not self.qr_code_img:
#             qr_data = f"Batch: {self.batch_number}\nSerial: {self.serial_number}"
#             qr = qrcode.make(qr_data)
#             canvas = BytesIO()
#             qr.save(canvas, format='PNG')
#             filename = f'qr_code_{self.serial_number}.png'
#             self.qr_code_img.save(filename, File(canvas), save=False)
#             canvas.close()

#         # ✅ Step 4: Last main final save
#         super().save(*args, **kwargs)

#     def generate_serial_number(self):
#         """Random unique serial number generator"""
#         return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
from django.db import models
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile  # Safe for cloud storage
import random
import string

class DrugBatch(models.Model):
    batch_number = models.AutoField(primary_key=True)
    drug_name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    production_date = models.DateField()
    expiry_date = models.DateField()
    serial_number = models.CharField(max_length=100, unique=True, blank=True)
    qr_code_img = models.ImageField(upload_to='qr_codes/', blank=True)

    def __str__(self):
        return f"{self.drug_name} - Batch {self.batch_number}"

    def save(self, *args, **kwargs):
        # If serial not set, generate it
        if not self.serial_number:
            self.serial_number = self.generate_serial_number()

        # Save once to get a primary key if new
        if not self.pk:
            super().save(*args, **kwargs)

        # Generate QR code
        qr_data = f"Batch: {self.batch_number}\nSerial: {self.serial_number}"
        qr = qrcode.make(qr_data)
        canvas = BytesIO()
        qr.save(canvas, format='PNG')
        canvas.seek(0)

        filename = f'qr_code_{self.serial_number}.png'

        # Attach to ImageField
        self.qr_code_img.save(filename, ContentFile(canvas.read()), save=False)
        canvas.close()

        # Save final object
        super().save(*args, **kwargs)

    def generate_serial_number(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
