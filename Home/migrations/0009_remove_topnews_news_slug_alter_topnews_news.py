# Generated by Django 5.0.6 on 2024-05-24 21:23

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_alter_topnews_news_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topnews',
            name='news_slug',
        ),
        migrations.AlterField(
            model_name='topnews',
            name='news',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='get_news_title', unique=True),
        ),
    ]
