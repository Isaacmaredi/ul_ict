# Generated by Django 4.1.3 on 2023-01-05 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ict_contracts', '0007_remove_contract_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='created_by',
            field=models.CharField(editable=False, max_length=100, verbose_name='Created By'),
        ),
    ]