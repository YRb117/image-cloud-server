# Generated by Django 4.2.6 on 2023-10-17 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimage',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]