from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
import random
import string

class DrugBatch(models.Model):
    batch_number = models.AutoField(primary_key=True)
    drug_name = models.CharField(max_length=100)
    manufacturer =models.CharField(max_length=100)
    production_date =models.DateField()
    expiry_date =models.DateField()
    serial_number =models.CharField(max_length=100,unique=True,blank=True)
    qr_code_img = models.ImageField(upload_to='qr_codes/',blank=True)

    def __str__(self):
        return f"{self.drug_name} - Batch {self.batch_number}"
    
    def save(self,*args,**kwargs):
        if not self.serial_number:
            self.serial_number=self.generate_serial_number()


        # Step 2: if object is new, save first to get batch_number
        if not self.pk:
            super().save(*args, **kwargs)

        qr_data = f" Batch : { self.batch_number}\nSerial:{self.serial_number}"
        qr =  qrcode.make(qr_data)
        canvas = BytesIO()
        qr.save(canvas,format='PNG')
        filename =f'qr_code_{self.serial_number}.png'
        self.qr_code_img.save(filename,File(canvas),save=False)
        canvas.close()

        super().save(*args,**kwargs)
    
    def generate_serial_number(self):
        return ''.join(random.choices(string.ascii_uppercase +string.digits , k=12))

