from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory

# Create your tests here.
from django.urls import reverse

from vlog_app.admin import models
from vlog_app.models import *
from vlog_app.views import *


class VideoMethodTests(TestCase):
    def test_ensure_correct_input(self):
        tag1 = Tag(name='hot')
        tag1.save()
        video = Video(title='test', views=1, length = "00:56",tag = tag1)
        video.save()
        self.assertEqual(video.tag.name, "hot")

class TagMethodTests(TestCase):
    def test_ensure_correct_input(self):
        tag = Tag(name='hot')
        self.assertEqual(tag.name, "hot")

class ViewRegisterTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    def test_checkWeb(self):
        request = self.factory.get('')
        response = register(request)
        self.assertEqual(response.status_code, 200)


class ViewLoginTests(TestCase):
    def test_checkWeb(self):
        response = self.client.get(reverse('vlog:login'))
        self.assertEqual(response.status_code, 200)


class user_info_Tests(TestCase):

    def test_checkWeb(self):
        response = self.client.get(reverse('vlog:user_info'))
        self.assertEqual(response.status_code, 302)


class user_info_edit_Tests(TestCase):
    def test_checkWeb(self):
        response = self.client.get(reverse('vlog:user_info_edit'))
        self.assertEqual(response.status_code, 302)

class change_password_Tests(TestCase):
    def test_checkWeb(self):
        response = self.client.get(reverse('vlog:change_password'))
        self.assertEqual(response.status_code, 302)

class home_Tests(TestCase):
    def test_checkWeb(self):
        response = self.client.get(reverse('vlog:home'))
        self.assertEqual(response.status_code, 200)

class video_list_result_Tests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    def test_checkWeb(self):
        request = self.factory.get('')
        response = video_list_result(request,1)
        self.assertEqual(response.status_code, 200)

class video_detail_Tests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    def test_checkWeb(self):
        request = self.factory.get('')
        response = video_list_result(request,1)
        self.assertEqual(response.status_code, 200)





