# Generated by Django 3.0.8 on 2020-08-05 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(default='', max_length=250),
        ),
    ]