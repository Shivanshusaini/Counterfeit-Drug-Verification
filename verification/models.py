from django.db import models
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
import random
import string
import tempfile
import os
from .utils import upload_qr_to_supabase

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
        if not self.serial_number:
            self.serial_number = self.generate_serial_number()

        if not self.pk:
            super().save(*args, **kwargs)

        qr_data = f"Batch: {self.batch_number}\nSerial: {self.serial_number}"
        qr = qrcode.make(qr_data)
        canvas = BytesIO()
        qr.save(canvas, format='PNG')
        canvas.seek(0)

        filename = f'qr_code_{self.serial_number}.png'
        local_path = f'qr_codes/{filename}'

        # ✅ Local remove if exists
        if self.qr_code_img and self.qr_code_img.name == local_path:
            self.qr_code_img.delete(save=False)

        # ✅ Local save
        self.qr_code_img.save(filename, ContentFile(canvas.read()), save=False)

        # ✅ Supabase overwrite
        canvas.seek(0)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
            tmp_file.write(canvas.getvalue())
            tmp_file.flush()
            tmp_file.close()

            self.qr_code_url = upload_qr_to_supabase(filename, tmp_file.name)

            os.remove(tmp_file.name)

        canvas.close()

        super().save(*args, **kwargs)

    def generate_serial_number(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
