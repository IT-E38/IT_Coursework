from django.urls import path

from vlog_app import views

app_name = 'vlog'

urlpatterns = [
    path('', views.user_login),
    path('login/', views.user_login,name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register),
    path('user_info/', views.user_info,name = 'user_info'),
    path('user_info_edit/', views.user_info_edit,name='user_info_edit'),
    path('admin_info/', views.admin_info),
    path('home/', views.home,name='home'),
    path('video_list/<video_type>/', views.video_list_result, name='video_list'),
    path('video_detail/<video_id>/', views.video_detail),
    path('user_manage/', views.user_manage),
    path('user_manage/<id_or_name>/', views.user_manage_query, name='user_manage'),
    path('video_manage/', views.video_manage),
    path('video_manage/<id_or_title>/', views.video_manage_query, name='video_manage'),
    path('video_add/', views.video_add),  # return to video_add.html page view
    path('add_video/', views.add_video),  # admin add a video
    path('user_add/', views.user_add),  # return to user_add.html page view
    path('add_user/', views.add_user),  # admin add a user
    path('update_user/', views.update_user),  # user update theirs own info
    path('update_admin/', views.update_admin),  # admin update theirs own info
    path('update_video/', views.update_video),  # return to video_update.html page view
    path('update_video_info/', views.update_video_info),  # admin update video
    path('delete_video/<video_id>/', views.delete_video),  # admin delete video
    path('update_user_page/', views.update_user_page),  # admin update user
    path('update_user_info/', views.update_user_info),  # admin update user
    path('delete_user/<user_id>/', views.delete_user),  # admin delete user
]
