import json
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
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
                'lastSync',
                'jumlahSync',
                'pd',
                'rombel',
                'guru',
                'pegawai',
                'rKelas',
                'rLab',
                'rPerpus']

def dataSekolah(request):
    context = {
        'posts': Post.objects.all(),
        'posts': Post.objects.order_by('-lastSync')
    }

    return render(request, 'mainapp/data_sekolah.html', context)

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
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
                'rPerpus']

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/datasekolah'