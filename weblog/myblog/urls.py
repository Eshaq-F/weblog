from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'myblog'

urlpatterns = [
    path('', views.home, name='home'),
    path('view_post/<int:post_id>/', views.view_post, name='view_post'),
    path('add_post/', views.add_post, name='add_post'),
]
