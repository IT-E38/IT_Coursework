from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    dob = models.DateField()
    description = models.CharField(max_length=255, blank=True,null=True)

    def __str__(self):
     return self.user.username


class Tag(models.Model):
    name = models.CharField(max_length=128, unique=True)
    # slug = models.SlugField(blank=True)
    #
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255,blank=True,null=True)
    length = models.TimeField(null = True)
    views = models.IntegerField(default=0,blank=True)
    # likes = models.IntegerField(default=0)
    likes = models.ManyToManyField(User,blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    file = models.FileField(upload_to='video/',null=True)
    picture = models.ImageField(upload_to="video_picture/")
    release_date = models.DateTimeField(auto_now_add=True, blank=True, max_length=20)


    def __str__(self):
        return self.title


    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])


# class Manager(models.Model):
#     manager = models.OneToOneField(User, on_delete=models.CASCADE)
#     email = models.EmailField(blank=True)
#     dob = models.DateField()
#     description = models.CharField(max_length=255, blank=True)
