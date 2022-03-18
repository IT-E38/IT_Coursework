import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'django_pages_project.settings')

import django

django.setup()

from vlog_app.models import Tag, Video


def populate():


    tag_pages = [{"name":"Food"},{"name":"Travel"}]

    video_pages = [{"title": "TestData1", "description": "IT_Coursework", "length": "00:32:56","views": 0 ,"tag":"Food",
         "file":"video/nature.mp4","picture":"video_picture/WechatIMG38586.jpg",},
                   {"title": "TestData2", "description": "IT_Coursework", "length": "00:32:56", "views": 0, "tag": "Travel",
                    "file": "video/nature.mp4", "picture": "video_picture/WechatIMG38586.jpg", },
                   ]

    for tag in tag_pages:
        print(tag)
        add_tag(tag["name"])

    for video_data in video_pages:
        print(video_data)
        add_video(video_data["title"],video_data["description"],video_data["length"],
                       video_data["views"],video_data["tag"],video_data["file"],
                      video_data["picture"],)


def add_tag(name):
        tag = Tag.objects.get_or_create(name=name)
        return tag


def add_video(title,description,length,views,tag,file,picture):
    video = Video.objects.get_or_create(title=title)[0]
    print(video)
    print(video.description)
    tagID = Tag.objects.get(name=tag)
    print(tagID.id)
    video.description = description
    video.length = length
    video.views = views
    video.tag_id = tagID.id
    video.file = file
    video.picture = picture
    video.save()
    return video


if __name__ == '__main__':
    print('Starting vlog_app population script...')
    populate()
    print('Populate Successful')
