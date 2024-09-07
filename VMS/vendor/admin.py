from django.contrib import admin
from vendor.models import Vendor
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Vendor)
class VendorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name','vendor_code','contact_details','address','quality_rating_avg',]
    search_fields = ['name','vendor_code','contact_details']