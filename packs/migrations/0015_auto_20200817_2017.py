# Generated by Django 3.0.8 on 2020-08-17 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packs', '0014_auto_20200817_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pack',
            name='publish_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]