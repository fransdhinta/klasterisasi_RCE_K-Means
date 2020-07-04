# Generated by Django 3.0.3 on 2020-06-14 04:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20200614_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rasioGRB',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(999)], verbose_name='Rasio Guru / Rombel'),
        ),
        migrations.AlterField(
            model_name='post',
            name='rasioPDRB',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(999)], verbose_name='Rasio Peserta Didik / Rombel'),
        ),
    ]
