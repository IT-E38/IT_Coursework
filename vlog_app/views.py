import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.contrib.auth.hashers import check_password
from django.db.models import Q

from vlog_app.models import Tag,Video,UserProfile,User
from vlog_app.forms import *
from django_pages_project import settings


"""

User Module

"""


def register(request):
    """
    For User Register
    """
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect(reverse('vlog:login'))
        else:
            print(user_form.errors)
    else:
        user_form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
    return render(request, 'register.html', {'user_form':user_form,
                                            'profile_form':profile_form,})


def user_login(request):
    """
    For User Login
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username = username)
        pwd = user.password
        print(user.username,pwd)
        print(password)
        print(bool(check_password(password,pwd)))
        user = authenticate(username = username,password = password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect(reverse('vlog:home'))
            else:
                return HttpResponse('Your VlogWeb account is disabled')
        else:
            print(user)
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
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
    user_profile = UserProfile.objects.get(user = user)
    print(user_profile.dob)
    return render(request, 'user_info.html', {'user': user,'user_profile':user_profile})


@login_required
def user_info_edit(request):
    """
    For User information edit
    """
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST)

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
        form = ProfileEditForm(request.POST)
    return render(request, 'user_info_edit.html', {'form': form})


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
    video = Video.objects.get(id = video_id)
    video.increase_views()
    print(video.views)
    return render(request, 'video_detail.html', {'video': video_detail})


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




"""

Admin module

"""

def admin_info(request):
    # todo: login admin.

    admin = {'username': 'Tom Smith', 'introduction': 'A user from world.', 'date': '1999-01-01',
             'email': 'xjjiofjiosjfiosjaio@email.com', 'password': 'xxxxxxxxxxxxxxxxx'}
    return render(request, 'admin_info.html', {'admin': admin})




def user_manage(request):
    return render(request, 'user_manage.html')


def user_manage_query(request, id_or_name):
    print('condition:', id_or_name)
    user_objs = [
        {'id': 1, 'userphoto': 'images/user.png', 'username': 'name', 'password': 'xxxxxxxx', 'email': 'email@qq.com',
         'introduction': 'xjiofjioasjiofa', 'date': '2022-03-05'},
        {'id': 2, 'userphoto': 'images/user.png', 'username': 'name', 'password': 'xxxxxxxx', 'email': 'email@qq.com',
         'introduction': 'xjiofjioasjiofa', 'date': '2022-03-05'},
    ]
    return render(request, 'user_manage.html', {'user_objs': user_objs})


def video_manage(request):
    return render(request, 'video_manage.html')


def video_manage_query(request, id_or_title):
    print('query_conditions:', id_or_title)

    video_objs = [
        {'id': 1, 'photo': 'images/cat.png', 'title': 'name', 'url': 'dadaa.mp4', 'classify': 'food',
         'introduction': 'xxxxxx', 'date': '2022-03-14 13:12:54'},
        {'id': 2, 'photo': 'images/cat.png', 'title': 'name', 'url': 'dadaa.mp4', 'classify': 'food',
         'introduction': 'xxxxxx', 'date': '2022-03-14 13:12:54'},
    ]
    return render(request, 'video_manage.html', {'video_objs': video_objs})


def video_add(request):
    return render(request, 'video_add.html')


def add_video(request):
    # todo: Handle the post request of new video in the foreground,  which is similar to the request of new users below.
    new_video_obj = {}
    # ....

    return render(request, 'video_manage.html', {'video_objs': new_video_obj})


def user_add(request):
    """
    return to user_add.html page views.
    :param request: request obj
    :return: the view of user_add.html
    """
    return render(request, 'user_add.html')


def add_user(request):
    """
    Handle add user operation from post request.
    :param request: request object.
    :return: render to user_manage.html attach the new user object.
    """
    user = {}
    if request.method == 'POST':
        print(request.POST)
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        introduction = request.POST.get('introduction')
        date = request.POST.get('date')
        image = request.FILES.get('photo')
        path = os.path.join('images', user_name + '.' + image.name.split('.')[-1])
        with open(os.path.join(settings.STATIC_DIR, path), 'wb') as f:
            for info in image.chunks():
                f.write(info)

        user = {'id': 1, 'userphoto': path, 'username': user_name, 'password': password, 'email': email,
                'introduction': introduction, 'date': date}

    return render(request, 'user_manage.html', {'user_objs': [user]})


def update_user(request):
    # todo: Replace with your own code to update user information.
    user = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        introduction = request.POST.get('introduction')
        date = request.POST.get('date')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = {'username': username, 'introduction': introduction, 'date': date, 'email': email, 'password': password}

    print(user)
    return render(request, 'user_info.html', {'user': user})


def update_admin(request):
    # todo: Replace with your own code to update admin information.
    admin = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        introduction = request.POST.get('introduction')
        date = request.POST.get('date')
        email = request.POST.get('email')
        password = request.POST.get('password')

        admin = {'username': username, 'introduction': introduction, 'date': date, 'email': email, 'password': password}

    print(admin)
    return render(request, 'admin_info.html', {'admin': admin})


def update_video(request):
    video = {}
    if request.method == 'POST':
        id = request.POST.get('id')
        photo = request.POST.get('photo')
        title = request.POST.get('title')
        url = request.POST.get('url')
        classify = request.POST.get('classify')
        introduction = request.POST.get('introduction')
        date = request.POST.get('date')
        video = {'id': id, 'photo': photo, 'title': title, 'url': url, 'classify': classify,
                 'introduction': introduction, 'date': date}

    return render(request, 'video_update.html', {'video': video})


def update_video_info(request):
    """
    After updating the information, return to the video management interface and carry the updated video information.
    :param request:
    :return:
    """
    video = {}
    if request.method == 'POST':
        id = request.POST.get('id')
        photo = request.POST.get('photo')
        title = request.POST.get('title')
        url = request.POST.get('url')
        classify = request.POST.get('classify')
        introduction = request.POST.get('introduction')
        date = request.POST.get('date')

        # todo: For the newly uploaded video, you can choose to overwrite the previous video or not. If you overwrite it
        #  , you can modify the URL, photo and other information of the corresponding video, and then store it in the
        #  database.
        video_file = request.FILES.get('video')  #
        if video_file is not None:
            path = os.path.join(settings.MEDIA_ROOT, video_file.name)
            with open(path, 'wb') as f:
                for info in video_file.chunks():
                    f.write(info)

        video = {'id': id, 'photo': photo, 'title': title, 'url': url, 'classify': classify,
                 'introduction': introduction, 'date': date}

    # return render(request, 'video_manage.html', {'video_objs': [video]})
    return redirect('vlog:video_manage', id_or_title=video['id'])  # 重定向


def delete_video(request, video_id):
    print('delete video id:', video_id)
    # todo: Complete the business logic code of deleting video

    return render(request, 'video_manage.html', {'msg': 'Delete succeeded!'})


def update_user_page(request):
    user = {}
    if request.method == 'POST':
        id = request.POST.get('id')
        userphoto = request.POST.get('userphoto')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        introduction = request.POST.get('introduction')
        date = request.POST.get('date')
        user = {'id': id, 'userphoto': userphoto, 'username': username, 'password': password, 'email': email,
                'introduction': introduction, 'date': date}

    return render(request, 'user_update.html', {'user': user})


def update_user_info(request):
    """
    After updating the information, return to the user management interface and carry the updated user information.
    :param request:
    :return:
    """
    user = {}
    if request.method == 'POST':
        id = request.POST.get('id')
        userphoto = request.POST.get('userphoto')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        introduction = request.POST.get('introduction')
        date = request.POST.get('date')

        # todo: For the newly uploaded image, you can choose to overwrite the previous image or not. If you overwrite it
        #  , you can modify the URL, photo and other information of the corresponding video, and then store it in the
        #  database.
        image_file = request.FILES.get('photo')  #
        if image_file is not None:
            path = os.path.join(settings.STATIC_DIR, image_file.name)
            with open(path, 'wb') as f:
                for info in image_file.chunks():
                    f.write(info)

        user = {'id': id, 'userphoto': userphoto, 'username': username, 'password': password, 'email': email,
                'introduction': introduction, 'date': date}

    # return render(request, 'video_manage.html', {'video_objs': [video]})
    return redirect('vlog:user_manage', id_or_name=user['id'])  # 重定向


def delete_user(request, user_id):
    print('delete user id:', user_id)
    # todo: Complete the business logic code of deleting user

    return render(request, 'user_manage.html', {'msg': 'Delete succeeded!'})
