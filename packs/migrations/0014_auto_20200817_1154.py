# Generated by Django 3.0.8 on 2020-08-17 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packs', '0013_auto_20200816_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pack',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='pack',
            name='sample_track',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
