# Generated by Django 4.1.3 on 2023-03-03 19:11

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ict_licenses', '0017_alter_license_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='LicenseRenewal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('renewal_date', models.DateField()),
                ('renewal_amount', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=8)),
                ('pr_number', models.CharField(blank=True, max_length=30, null=True)),
                ('po_number', models.CharField(max_length=30)),
                ('is_paid', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('license', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='renewals', to='ict_licenses.license')),
            ],
        ),
        migrations.DeleteModel(
            name='Renewal',
        ),
    ]