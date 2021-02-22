from django.conf.urls import url
from django.urls import path
from . import views
from . import views_api

app_name = 'myblog'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('view_post/<int:post_id>/', views.view_post, name='view_post'),
    path('add_post/', views.add_post, name='add_post'),
    path('post_by_category/<int:category_id>/', views.post_by_category, name='post_by_category'),
    path('post_by_tag/<int:tag_id>/', views.post_by_tag, name='post_by_tag'),
    path('comment_like_dislike/<int:pk>/', views_api.LikeCommentLogList.as_view(), name='comment_like_dislike'),
]
