# Generated by Django 4.1.3 on 2023-02-25 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ict_licenses', '0013_alter_license_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='license',
            options={'ordering': ('-current_cost',)},
        ),
    ]