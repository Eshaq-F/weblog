from django.urls import path
from . import views
from . import views_api

app_name = 'myblog'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('simple_search/', views.simple_search, name='simple_search'),
    path('advanced_search/', views.advanced_search, name='advanced_search'),
    path('view_post/<int:post_id>/', views.view_post, name='view_post'),
    path('add_post/', views.add_post, name='add_post'),
    path('post_by_category/<int:category_id>/', views.post_by_category, name='post_by_category'),
    path('post_by_tag/<int:tag_id>/', views.post_by_tag, name='post_by_tag'),
    path('comment_like_dislike/<int:pk>/', views_api.LikeCommentLogList.as_view(), name='comment_like_dislike'),
    path('comment_like_dislike/', views_api.LikeCommentLogList.as_view(), name='comment_like_dislike'),
    path('post_like_dislike/<int:pk>/', views_api.LikePostLogList.as_view(), name='post_like_dislike'),
    path('post_like_dislike/', views_api.LikePostLogList.as_view(), name='post_like_dislike'),
]
