# Generated by Django 4.0.5 on 2022-07-03 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gis_app', '0009_alter_city_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
