# Generated by Django 3.0.3 on 2020-05-04 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_kecamatan'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pilihKecamatan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.kecamatan'),
        ),
    ]