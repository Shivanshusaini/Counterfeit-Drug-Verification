# from django.contrib import admin
# from .models import DrugBatch

# admin.site.register(DrugBatch)
from django.contrib import admin
from django.utils.html import format_html
from .models import DrugBatch

@admin.register(DrugBatch)
class DrugBatchAdmin(admin.ModelAdmin):
    list_display = ('drug_name', 'batch_number', 'serial_number', 'qr_code_preview')

    # def qr_code_preview(self, obj):
    #     if obj.qr_code_img:
    #         return format_html('<img src="{}" width="120" />', obj.qr_code_img.url)
    #     return "-"
    # qr_code_preview.short_description = "QR Code"

    def qr_code_preview(self, obj):
        if obj.qr_code_url:
            return format_html('<img src="{}" width="120" />', obj.qr_code_url)
        elif obj.qr_code_img:
            return format_html('<img src="{}" width="120" />', obj.qr_code_img.url)
        return "-"
