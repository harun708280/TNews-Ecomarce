# Generated by Django 5.0.6 on 2024-05-25 10:23

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_super_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topnews',
            name='news',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='news_title', unique=True),
        ),
    ]
