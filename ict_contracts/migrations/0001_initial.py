# Generated by Django 4.1.3 on 2022-11-12 21:06

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ict_vendors', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ict_accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('total_value', models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=10, verbose_name='Contract Value')),
                ('amount_outstanding', models.DecimalField(decimal_places=2, default=Decimal('0.0'), editable=False, max_digits=10, verbose_name='Amount Outstanding')),
                ('agreement_type', models.CharField(choices=[(None, 'Select agreement type'), ('Master Service Agreement', 'Master Service Agreement'), ('Service Level Agreement', 'Service Level Agreement'), ('Fixed Contract', 'Fixed Contract'), ('Subscription Agreement', 'Subscription Agreement'), ('Pay-per-Use', 'Pay-per-Use')], max_length=150, verbose_name='Agreement Type')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(default='Ok', editable=False, max_length=300)),
                ('date_signed', models.DateField(blank=True, null=True)),
                ('ul_signatory', models.CharField(max_length=300, verbose_name='UL Signatory')),
                ('supplier_signatory', models.CharField(max_length=300, verbose_name='Supplier Signatory')),
                ('contract_document', models.FileField(upload_to='contracts/%Y/%F')),
                ('comments', models.TextField()),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(max_length=300, on_delete=django.db.models.deletion.DO_NOTHING, to='ict_accounts.profile', verbose_name='Responsible Manager')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='vendors', to='ict_vendors.vendor')),
            ],
            options={
                'ordering': ('-uploaded',),
            },
        ),
    ]
