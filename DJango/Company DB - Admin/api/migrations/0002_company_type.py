# Generated by Django 4.2.13 on 2024-05-28 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='type',
            field=models.CharField(choices=[('IT', 'IT'), ('Non IT', 'Non IT'), ('Mobile Phones', 'Mobile Phones')], default='IT', max_length=100),
        ),
    ]