from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'myblog'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('view_post/<int:post_id>/', views.view_post, name='view_post'),
    path('add_post/', views.add_post, name='add_post'),
    path('all_posts/', views.post_collection, name='all_posts'),
    path('post_by_category/<int:category_id>/', views.post_by_category, name='post_by_category'),
]
