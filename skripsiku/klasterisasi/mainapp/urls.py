from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import PostCreateView, PostDetailView
from . import views

urlpatterns = [
    path('', views.home, name='mainapp-home'),
    path('post/new/',login_required(PostCreateView.as_view(template_name="mainapp/post_form.html")),name='post-create')
]