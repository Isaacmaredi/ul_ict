# Generated by Django 4.1.3 on 2023-02-25 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ict_contracts', '0012_alter_contract_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contract',
            options={'ordering': ('total_value',)},
        ),
    ]
