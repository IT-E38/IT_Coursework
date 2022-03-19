import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'django_pages_project.settings')

import django
django.setup()
from vlog_app.models import Tag, Video

def populate():
    tag_pages = [{"name": "Food"},
                 {"name": "Travel"},
                 {"name": "Study"},
                 {"name": "Travel"},
                 {"name": "DailyLife"},
                 ]

    video_pages = [
        {"title": "48 HOURS IN PARIS", "description": "This is a big one for us. We went to Paris for 48 hours and had a very, very good time. It’s a sweet 16 minutes long and we think it’s our favourite one yet.", "length": "00:16:13", "views": 98, "tag": "Travel",
         "file": "video/video2.mov", "picture": "video_picture/testimg1.jpg", },
        {"title": "STUDY WITH ME IN SHIBUYA", "description": "Study with me ", "length": "01:56:53", "views": 50, "tag": "Study",
         "file": "video/video1.mp4", "picture": "video_picture/testimg2.jpg", },
        {"title": "FIGURING OUT MY LIFE", "description": "Share My Daily Life", "length": "00:04:07", "views": 40, "tag": "Study",
         "file": "video/video1.mp4", "picture": "video_picture/testimg3.jpg", },
        {"title": "LEARN HOW TO SPEECH", "description": "Learn how to make a conversation with others", "length": "00:12:58", "views": 30, "tag": "Study",
         "file": "video/video1.mp4", "picture": "video_picture/testimg4.jpg", },
        {"title": "TULUM VLOG", "description": "An unforgettable travel experience", "length": "00:28:37", "views": 20, "tag": "Travel",
         "file": "video/video1.mp4", "picture": "video_picture/testimg5.jpg", },
        {"title": "24 HOURS IN LIVERPOOL", "description": "24 hours amazing trip in LR", "length": "00:15:01", "views": 10, "tag": "Travel",
         "file": "video/video1.mp4", "picture": "video_picture/testimg6.jpg", },
        {"title": "48 HOURS IN EDINBURH", "description": "I love Edinburgh", "length": "00:15:42", "views": 5, "tag": "Travel",
         "file": "video/video1.mp4", "picture": "video_picture/testimg7.jpg", },
        {"title": "FASTER SNACKS EVER", "description": "Learn how to cook snacks", "length": "00:11:36", "views": 0, "tag": "Food",
         "file": "video/video1.mp4", "picture": "video_picture/testimg8.jpg", },
        ]

    for tag in tag_pages:
        print(tag)
        add_tag(tag["name"])

    for video_data in video_pages:
        print(video_data)
        add_video(video_data["title"], video_data["description"], video_data["length"],
                  video_data["views"], video_data["tag"], video_data["file"],
                  video_data["picture"], )


def add_tag(name):
    tag = Tag.objects.get_or_create(name=name)
    return tag


def add_video(title, description, length, views, tag, file, picture):
    tagid = Tag.objects.get(name=tag)
    video = Video.objects.get_or_create(title=title,tag=tagid)[0]
    print(video)
    print(video.description)
    tagid = Tag.objects.get(name=tag)
    print(tagid.id)
    video.description = description
    video.length = length
    video.views = views
    video.file = file
    video.picture = picture
    video.save()
    return video


if __name__ == '__main__':
    print('Starting vlog_app population script...')
    populate()
    print('Populate Successful')
