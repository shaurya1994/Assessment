# Generated by Django 4.2.13 on 2024-05-28 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_employee_about_remove_employee_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('MNG', 'Manager'), ('SD', 'Software Developer'), ('PL', 'Project Leader')], default='Software Developer', max_length=50),
        ),
    ]
