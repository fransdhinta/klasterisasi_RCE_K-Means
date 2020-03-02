import json
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'mainapp/home.html', {'title': 'Hello'})
