# Generated by Django 4.2.1 on 2023-06-19 12:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_journalfilesurl_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsurl',
            name='published_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='newsurl',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsurl',
            name='status',
            field=models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2),
        ),
        migrations.AddField(
            model_name='newsurl',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='newsurl',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]