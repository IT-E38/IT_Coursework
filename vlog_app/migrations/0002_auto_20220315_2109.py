# Generated by Django 2.1.5 on 2022-03-15 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vlog_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='manager',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='video',
            name='Views',
        ),
        migrations.RemoveField(
            model_name='video',
            name='url',
        ),
        migrations.AddField(
            model_name='video',
            name='file',
            field=models.FileField(null=True, upload_to='video/'),
        ),
        migrations.AddField(
            model_name='video',
            name='views',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='video',
            name='picture',
            field=models.ImageField(upload_to='video_picture/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vlog_app.Tag'),
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
    ]
