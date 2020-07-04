from django import forms
from .models import Post

class KecamatanForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['pilihKecamatan']

class BPForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['bp']

class DataForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['namaSekolah',
                'npsn',
                'bp',
                'status',
                'lastSync',
                'jumlahSync',
                'pd',
                'rombel',
                'guru',
                'pegawai',
                'rKelas',
                'rLab',
                'rPerpus',
                'rasioPDRB',
                'rasioGRB',
                'pilihKecamatan']