# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndexImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_name', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to=b'static/user_data/')),
                ('image_hires', models.ImageField(upload_to=b'static/user_data/')),
                ('title', models.CharField(max_length=140)),
                ('caption', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='IndexMosiac',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mosiac_name', models.CharField(default=b'my_mosiac', max_length=50)),
                ('image1', models.ForeignKey(related_name='image1', to='basefunctions.IndexImage')),
                ('image2', models.ForeignKey(related_name='image2', to='basefunctions.IndexImage')),
                ('image3', models.ForeignKey(related_name='image3', to='basefunctions.IndexImage')),
                ('image4', models.ForeignKey(related_name='image4', to='basefunctions.IndexImage')),
                ('image5', models.ForeignKey(related_name='image5', to='basefunctions.IndexImage')),
                ('image6', models.ForeignKey(related_name='image6', to='basefunctions.IndexImage')),
                ('image7', models.ForeignKey(related_name='image7', to='basefunctions.IndexImage')),
                ('image8', models.ForeignKey(related_name='image8', to='basefunctions.IndexImage')),
                ('image9', models.ForeignKey(related_name='image9', to='basefunctions.IndexImage')),
            ],
        ),
    ]
