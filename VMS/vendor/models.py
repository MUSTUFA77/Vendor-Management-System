from django.db import models
import uuid
# Create your models here.

def generate_uuid():
    return str(uuid.uuid4())

class Vendor(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    contact_details = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    vendor_code = models.CharField(max_length=255, null=True, blank=True, unique=True)
    on_time_delivery_rate = models.FloatField(null=True, blank=True)
    quality_rating_avg = models.FloatField(null=True, blank=True)
    average_response_time = models.FloatField(null=True, blank=True)
    fulfillment_rate = models.FloatField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    vendor_uuid = models.CharField(max_length=255, blank=True, null=True, default=generate_uuid)

    class Meta:
        db_table = 'vms_vendor'
        verbose_name = 'VMS Vendor'
        verbose_name_plural = 'VMS Vendors'
    
    def __str__(self):
        return str(self.name)