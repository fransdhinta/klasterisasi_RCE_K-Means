from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import PostCreateView, PostDetailView, PostUpdateView, PostDeleteView
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='mainapp-home'),
    path('klasterisasi', login_required(views.klasterisasi), name='mainapp-klasterisasi'),
    # path('post/new/',login_required(PostCreateView.as_view(template_name="mainapp/post_form.html")),name='post-create'),
    path('post/<int:pk>/',login_required(PostDetailView.as_view(template_name="mainapp/post_detail.html")),name='post-detail'),
    path('datasekolah',login_required(views.dataSekolah), name='data-sekolah'),
    path('datasekolah_u',views.dataSekolah_u, name='data-sekolah-u'),
    path('post/<int:pk>/update',login_required(PostUpdateView.as_view(template_name="mainapp/post_form.html")),name='post-update'),
    path('post/<int:pk>/delete',login_required(PostDeleteView.as_view()),name='post-delete'),
    path('upload/csv', views.upload_csv, name='upload_csv'),
    # path('dataklaster', views.dataklaster, name='dataklaster'),
    # path('update/<int:pk>/', views.updateDataForm, name='update-data'),
    # url(r'^cobaAjax/$', views.cobaAjax, name='cobaAjax'),
]