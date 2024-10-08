# Generated by Django 4.2.1 on 2024-09-07 13:46

from django.db import migrations, models
import vendor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vendor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("contact_details", models.TextField(blank=True, null=True)),
                ("address", models.TextField(blank=True, null=True)),
                (
                    "vendor_code",
                    models.CharField(
                        blank=True, max_length=255, null=True, unique=True
                    ),
                ),
                ("on_time_delivery_rate", models.FloatField(blank=True, null=True)),
                ("quality_rating_avg", models.FloatField(blank=True, null=True)),
                ("average_response_time", models.FloatField(blank=True, null=True)),
                ("fulfillment_rate", models.FloatField(blank=True, null=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "vendor_uuid",
                    models.CharField(
                        blank=True,
                        default=vendor.models.generate_uuid,
                        max_length=255,
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "VMS Vendor",
                "verbose_name_plural": "VMS Vendors",
                "db_table": "vms_vendor",
            },
        ),
    ]
