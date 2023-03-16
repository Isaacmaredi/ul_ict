# Generated by Django 4.1.3 on 2023-01-27 14:49

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ict_licenses', '0009_alter_license_next_renewal_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='license',
            old_name='renewal',
            new_name='is_renewed',
        ),
        migrations.AlterField(
            model_name='license',
            name='pricing_model',
            field=models.CharField(choices=[('Retainer', 'Retainer'), ('Seats', 'Seats'), ('Cores', 'Cores'), ('Minutes', 'Minutes'), ('Storage', 'Storage'), ('Minutes & Storage', 'Minutes & Storage')], max_length=200, verbose_name='Pricing Model'),
        ),
        migrations.AlterField(
            model_name='license',
            name='renewal_term',
            field=models.CharField(choices=[('Annual Renewal', 'Annual Renewal'), ('Once-Off', 'Once-Off'), ('Term Contract', 'Term Contract')], max_length=250, verbose_name='Renewal Term'),
        ),
        migrations.AlterField(
            model_name='license',
            name='software_category',
            field=models.CharField(choices=[('Productivity', 'Productivity'), ('Collaboration', 'Collaboration'), ('ERP', 'ERP'), ('CRM', 'CRM'), ('Learning Management System', 'Learning Management System'), ('Operating System', 'Operating System'), ('Database Management System', 'Database Management System'), ('Business Intelligence', 'Business Intelligence'), ('Data & Statistical Analytics', 'Data & Statistical Analytics'), ('Network Management', 'Network Management'), ('IT Service Management', 'IT Service Management'), ('Communication', 'Communication'), ('Collaboration', 'Collaboration'), ('Business Application', 'Business Application'), ('Academic Specialist Software', 'Academic Specialist Software')], max_length=250, verbose_name='Software Category'),
        ),
        migrations.AlterField(
            model_name='license',
            name='user_base',
            field=models.CharField(choices=[('Students', 'Students'), ('Academics', 'Academics'), ('Academics & Students', 'Academics & Students'), ('Admin Staff', 'Admin Staff'), ('Admin Staff & Students', 'Admin Staff & Students'), ('All Staff', 'All Staff'), ('All Staff & Students', 'All Staff & Students'), ('Academics Specialist', 'Academics Specialist'), ('ICT Staff', 'ICT Staff')], max_length=250, verbose_name='User Base'),
        ),
        migrations.CreateModel(
            name='Renewal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('renewal_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=8)),
                ('is_paid', models.BooleanField(default=False)),
                ('renewal_count', models.IntegerField(default=0, verbose_name='Renewal Count')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('license', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='renewals', to='ict_licenses.license')),
            ],
        ),
    ]