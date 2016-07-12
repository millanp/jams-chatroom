# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-26 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suggestionsapp', '0003_auto_20160624_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='label',
            field=models.SlugField(default='jyU5VMA97b7m', unique=True),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='title',
            field=models.CharField(max_length=182),
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='suggestionsapp.Chatroom'),
        ),
    ]