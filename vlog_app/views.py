import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.db.models import Q,Count
from django_pages_project import settings

from vlog_app.models import Tag,Video,UserProfile,User,Comment
from vlog_app.forms import *



"""

User Module

"""


def register(request):
    """
    For User Register
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect(reverse('vlog:login'))
        else:
            print(form.errors)
    else:
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
    return render(request, 'register.html', {'form':form,
                                            'profile_form':profile_form,})


def user_login(request):
    """
    For User Login
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect(reverse('vlog:home'))
            else:
                return HttpResponse('Your VlogWeb account is disabled')
        else:
            return HttpResponse('Your Vlogweb account username or password is incorrect')
    else:
        return render(request, 'index.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('vlog:login'))


@login_required
def user_info(request):
    """
    For User information display
    """
    user = request.user
    if user.is_superuser:
        return render(request, 'user_info.html', {'user': user, })
    user_profile = UserProfile.objects.get(user = user)
    user_starlist = user.video_set.all()
    return render(request, 'user_info.html', {'user': user,'user_profile':user_profile,'user_starlist':user_starlist})


@login_required
def user_info_edit(request):
    """
    For User information edit
    """
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST,instance=user_profile)

        if form.is_valid():
            user_profile.dob = form.cleaned_data['dob']
            user_profile.description = form.cleaned_data['description']
            user.email = form.cleaned_data['email']
            user.save()
            user_profile.save()
            return redirect(reverse('vlog:user_info'))

        else:
            print(form.errors)
    else:
        form = ProfileEditForm(request.POST,instance=user_profile)
    return render(request, 'user_info_edit.html', {'form': form,'user_profile':user_profile})


@login_required
def change_password(request):
    """
    For User password change
    """
    user = request.user
    if request.method == 'POST':
        form = PasswordEditForm(request.POST)
        if form.is_valid():
            initial_pwd = form.cleaned_data['password']
            new_pwd = form.cleaned_data['password1']
            print(initial_pwd)
            print(new_pwd)
            user = authenticate(username=user.username, password=initial_pwd)
            if user:
                user.set_password(new_pwd)
                user.save()
                return redirect(reverse('vlog:user_info'))
            else:
                return HttpResponse("invalid initial Password .")
        else:
            print(form.errors)
    else:
        form = PasswordEditForm(request.POST)
    return render(request, 'change_password.html', {'form': form,'user':user})



"""

Video module

"""


def home(request):
    all_videos =  Video.objects.order_by('-views')
    user = request.user
    return render(request, 'home.html', {'all_videos': all_videos,'user':user})


def video_list_result(request, tag_id):
    video_list = Video.objects.filter(tag = tag_id)
    return render(request, 'video_list_result.html', {'video_list': video_list})


def video_detail(request, video_id):
    video_detail = Video.objects.filter(id = video_id)
    user =request.user
    video = Video.objects.get(id = video_id)
    video.increase_views()
    comment = video.comment_set.order_by("-create_time")
    print(video.views)
    if user is not None:
        is_star = video.likes.filter(id = user.id).first()
    return render(request, 'video_detail.html', {'video': video_detail,'is_star':is_star,'comment':comment})


def video_moststar_list(request):
    all_videos = Video.objects.all().annotate(liker=Count('likes')).order_by('-liker')[:10]
    user = request.user
    print(all_videos)
    return render(request, 'video_moststar_list.html', {'all_videos': all_videos, 'user': user,})


@login_required
def user_star(request):
    """
    For User Star Video list display
    """
    user = request.user
    video_list = user.video_set.all().order_by('-views')
    print(video_list)
    return render(request, 'user_star.html',{'user': user, 'video_list': video_list})


def video_search(request):
    """
    For Video Search
    """
    if request.method == 'POST':
        search = request.POST["search"]
        request.session["search"] = search
    else:
        search = request.session.get("search")
    video_list = Video.objects.filter(
        Q(title__icontains=search) | Q(description__icontains=search) )
    return render(request,'video_search.html',{'video_list':video_list})


@login_required
def video_star(request,video_id):
    """
    For User Star Video
    """
    video = Video.objects.get(id = video_id)
    user = request.user
    video.likes.add(user)
    video.save()
    return redirect(reverse('vlog:video_detail',args=(video_id)))


@login_required
def video_destar(request,video_id):
    """
    For User Cancel Star Video
    """
    video = Video.objects.get(id = video_id)
    user = request.user
    video.likes.remove(user)
    video.save()
    return redirect(reverse('vlog:video_detail',args=(video_id)))


@login_required
def video_comment(request,video_id):
    """
    For User Star Video
    """
    video = Video.objects.get(id = video_id)
    user = request.user
    content = request.POST.get('comment')
    Comment.objects.create(user=user,video=video,content=content)
    return redirect(reverse('vlog:video_detail',args=(video_id)))

