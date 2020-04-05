from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.urls import reverse
from multiselectfield import MultiSelectField

# Create your models here.
BP_CHOICES = (
    ('SD', 'SD'),
    ('SMP', 'SMP'),
    ('SMA', 'SMA'),
    ('SMK', 'SMK')
)

STATUS_CHOICES = (
    ('NEGERI', 'NEGERI'),
    ('SWASTA', 'SWASTA')
)

class Post(models.Model):
    namaSekolah = models.CharField(verbose_name='Nama Sekolah', max_length=60, default='')
    npsn = models.PositiveIntegerField(verbose_name='NPSN', validators=[MaxValueValidator(999999999)], default=0)
    bp = models.CharField(verbose_name='BP', max_length=10, null=True, blank=True, choices=BP_CHOICES)
    status = models.CharField(verbose_name='STATUS', max_length=7, null=True, blank=True, choices=STATUS_CHOICES)
    lastSync = models.DateTimeField(default=timezone.now)
    jumlahSync = models.PositiveIntegerField(verbose_name='Jumlah Sync', null=True, blank=True, validators=[MaxValueValidator(999)], default=0)
    pd = models.PositiveIntegerField(verbose_name='Jumlah Peserta Didik', validators=[MaxValueValidator(99999)], default=0)
    rombel = models.PositiveIntegerField(verbose_name='Jumlah Rombongan Belajar', validators=[MaxValueValidator(99)], default=0)
    guru = models.PositiveIntegerField(verbose_name='Jumlah Guru', validators=[MaxValueValidator(999)], default=0)
    pegawai = models.PositiveIntegerField(verbose_name='Jumlah Pegawai', validators=[MaxValueValidator(999)], default=0)
    rKelas = models.PositiveIntegerField(verbose_name='Jumlah Ruang Kelas', validators=[MaxValueValidator(999)], default=0)
    rLab = models.PositiveIntegerField(verbose_name='Jumlah Ruang Lab.', validators=[MaxValueValidator(999)], default=0)
    rPerpus = models.PositiveIntegerField(verbose_name='Jumlah Ruang Perpustakaan', validators=[MaxValueValidator(999)], default=0)
    
    def __str__(self):
        return self.namaSekolah

    def get_absolute_url(self):
        return reverse('mainapp-home')