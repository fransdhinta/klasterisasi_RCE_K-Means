# Generated by Django 3.0.3 on 2020-05-04 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='kecamatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaKecamatan', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Nama Kecamatan')),
            ],
        ),
    ]
