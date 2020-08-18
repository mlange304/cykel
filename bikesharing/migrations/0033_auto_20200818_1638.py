# Generated by Django 2.2.13 on 2020-08-18 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bikesharing", "0032_auto_20200814_1732"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehicletype",
            name="form_factor",
            field=models.CharField(
                choices=[
                    ("BI", "Bike"),
                    ("ES", "E-Scooter"),
                    ("CA", "Car"),
                    ("MO", "Moped"),
                    ("OT", "Other"),
                ],
                default="BI",
                max_length=2,
            ),
        ),
    ]
