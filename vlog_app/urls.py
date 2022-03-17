from django.urls import path
from django.contrib import admin
from vlog_app import views

app_name = 'vlog'

urlpatterns = [
    path('', views.user_login),
    path('login/', views.user_login,name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register,name = 'register'),
    path('user_info/', views.user_info,name = 'user_info'),
    path('user_info_edit/', views.user_info_edit,name='user_info_edit'),
    path('change_password/', views.change_password,name='change_password'),
    path('home/', views.home,name = 'home'),
    path('video_list/<tag_id>/', views.video_list_result, name='video_list'),
    path('video_search/', views.video_search,name = 'video_search'),
    path('video_detail/<video_id>/', views.video_detail,name = 'video_detail'),
    path('video_star/<video_id>/', views.video_star,name = 'video_star'),
    path('video_destar/<video_id>/', views.video_destar, name = 'video_destar' ),
]
