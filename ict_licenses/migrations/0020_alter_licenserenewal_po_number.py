# Generated by Django 4.1.3 on 2023-03-03 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ict_licenses', '0019_alter_licenserenewal_renewal_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licenserenewal',
            name='po_number',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
