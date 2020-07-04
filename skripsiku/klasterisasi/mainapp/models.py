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

KECAMATAN_CHOICES = (
    ('Ampelgading', 'Ampelgading'),
    ('Bantur', 'Bantur'),
    ('Bululawang', 'Bululawang'),
    ('Dampit', 'Dampit'),
    ('Dau', 'Dau'),
    ('Donomulyo', 'Donomulyo'),
    ('Gedangan', 'Gedangan'),
    ('Gondanglegi', 'Gondanglegi'),
    ('Jabung', 'Jabung'),
    ('Kalipare', 'Kalipare'),
    ('Karangploso', 'Karangploso'),
    ('Kasembon', 'Kasembon'),
    ('Kepanjen', 'Kepanjen'),
    ('Kromengan', 'Kromengan'),
    ('Lawang', 'Lawang'),
    ('Ngajum', 'Ngajum'),
    ('Ngantang', 'Ngantang'),
    ('Pagak', 'Pagak'),
    ('Pagelaran', 'Pagelaran'),
    ('Pakis', 'Pakis'),
    ('Pakisaji', 'Pakisaji'),
    ('Poncokusumo', 'Poncokusumo'),
    ('Pujon', 'Pujon'),
    ('Sumbermanjing Wetan', 'Sumbermanjing Wetan'),
    ('Singosari', 'Singosari'),
    ('Sumberpucung', 'Sumberpucung'),
    ('Tajinan', 'Tajinan'),
    ('Tirtoyudo', 'Tirtoyudo'),
    ('Tumpang', 'Tumpang'),
    ('Turen', 'Turen'),
    ('Wagir', 'Wagir'),
    ('Wajak', 'Wajak'),
    ('Wonosari','Wonosari')
)

class kecamatan(models.Model):
    namaKecamatan = models.CharField(verbose_name='Nama Kecamatan', max_length=100, null=True, blank=True, default=None)

    def __str__(self):
        return self.namaKecamatan

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
    rasioPDRB = models.FloatField(verbose_name='Rasio Peserta Didik / Rombel', validators=[MaxValueValidator(999)], default=0)
    rasioGRB = models.FloatField(verbose_name='Rasio Guru / Rombel', validators=[MaxValueValidator(999)], default=0)
    pilihKecamatan = models.CharField(verbose_name='Pilih Kecamatan', max_length=100, null=True, blank=True, choices=KECAMATAN_CHOICES)

    def __str__(self):
        return self.namaSekolah

    def get_absolute_url(self):
        return reverse('data-sekolah', kwargs={})