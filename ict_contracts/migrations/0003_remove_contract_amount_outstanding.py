# Generated by Django 4.1.3 on 2022-12-06 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ict_contracts', '0002_remove_contract_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='amount_outstanding',
        ),
    ]
