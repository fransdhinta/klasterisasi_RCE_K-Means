from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import PostCreateView, PostDetailView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='mainapp-home'),
    path('post/new/',login_required(PostCreateView.as_view(template_name="mainapp/post_form.html")),name='post-create'),
    path('post/<int:pk>/',login_required(PostDetailView.as_view(template_name="mainapp/post_detail.html")),name='post-detail'),
    path('datasekolah',login_required(views.dataSekolah), name='data-sekolah'),
    path('post/<int:pk>/update',login_required(PostUpdateView.as_view(template_name="mainapp/post_form.html")),name='post-update'),
    path('post/<int:pk>/delete',login_required(PostDeleteView.as_view()),name='post-delete')
]