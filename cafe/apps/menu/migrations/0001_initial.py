# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-20 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u540d\u79f0')),
                ('kind', models.CharField(choices=[('english', '\u82f1\u56fd\u7d05\u8336'), ('chinese', '\u4e2d\u56fd\u8336'), ('japanese', '\u65e5\u672c\u8336')], max_length=255, verbose_name='\u7a2e\u985e')),
                ('price', models.IntegerField(verbose_name='\u4fa1\u683c')),
                ('is_recommended', models.BooleanField(default=False, verbose_name='\u304a\u52e7\u3081\u306e\u30e1\u30cb\u30e5\u30fc')),
            ],
        ),
    ]
