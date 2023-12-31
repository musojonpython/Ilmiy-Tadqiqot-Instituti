# Generated by Django 4.2.1 on 2023-06-30 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_newsurl_published_time_newsurl_slug_newsurl_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500)),
                ('image', models.ImageField(upload_to='bannerImages/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
