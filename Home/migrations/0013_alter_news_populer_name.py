# Generated by Django 5.0.6 on 2024-05-25 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_alter_news_populer_populer_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_populer',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
