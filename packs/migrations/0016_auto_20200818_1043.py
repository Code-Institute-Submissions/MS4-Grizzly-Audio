# Generated by Django 3.0.8 on 2020-08-18 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packs', '0015_auto_20200817_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(default=models.CharField(max_length=254), max_length=254),
        ),
        migrations.AlterField(
            model_name='pack',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='pack',
            name='sample_track',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
