import json
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView
from .models import Post


# Create your views here.
def home(request):
    return render(request, 'mainapp/home.html', {'title': 'Hello'})

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['namaSekolah',
                'npsn',
                'bp',
                'status',
                'npsn',
                'lastSync',
                'jumlahSync',
                'pd',
                'rombel',
                'guru',
                'pegawai',
                'rKelas',
                'rLab',
                'rPerpus']

class PostDetailView(DetailView):
    model = Post