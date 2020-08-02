# Generated by Django 3.0.8 on 2020-08-01 06:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('audio', models.FileField(upload_to='timeline_photo/%Y/%m/%d')),
                ('lyric', models.TextField()),
                ('view', models.PositiveIntegerField(default=0)),
                ('like', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
