# Generated by Django 4.1.3 on 2023-02-25 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ict_contracts', '0009_alter_contract_created_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contract',
            options={'ordering': ('-total_value',)},
        ),
    ]
