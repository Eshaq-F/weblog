from django.contrib.auth.views import LogoutView
from . import views
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('login/', views.signup_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
