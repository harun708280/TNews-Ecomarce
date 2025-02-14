# Generated by Django 5.0.6 on 2024-05-24 09:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_navimage'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('Create', models.CharField(blank=True, default='T-News', max_length=50, null=True)),
                ('descripton', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='News Image')),
                ('vedio', models.FileField(upload_to='Vedeos/')),
                ('total_views', models.IntegerField(blank=True, default=0, null=True)),
                ('cetagory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.cetagory', verbose_name='Add To Cetagory')),
                ('like', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
                ('sub_cetagory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.sub_cetagory', verbose_name='Sub Cetagory')),
            ],
            options={
                'verbose_name': 'Add to News',
            },
        ),
    ]
