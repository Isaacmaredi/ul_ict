# Generated by Django 4.1.3 on 2022-12-02 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ict_projects', '0010_alter_project_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-id']},
        ),
    ]
