# Generated by Django 3.2.7 on 2021-10-29 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211029_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentoseje',
            name='Contenido',
            field=models.FileField(upload_to='UploadedFiles/'),
        ),
    ]
