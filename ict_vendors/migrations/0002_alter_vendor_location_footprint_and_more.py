# Generated by Django 4.1.3 on 2023-01-12 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ict_vendors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='location_footprint',
            field=models.CharField(choices=[('LOCAL', 'Local'), ('MNC', 'Multinational Company'), ('FOREIGN', 'Foreign Based')], max_length=200, verbose_name='Company Footprint'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='supplier_channel',
            field=models.CharField(blank=True, choices=[('Direct-OEM', 'Direct-OEM'), ('INDIRECT-OEM', 'Indirect-OEM'), ('LSP', 'Licensed Solutions Provider'), ('LCR', 'Local Certified Reseller'), ('LSS', 'Local Sole Supplier ')], max_length=200, null=True, verbose_name='Supplier Channel'),
        ),
    ]
