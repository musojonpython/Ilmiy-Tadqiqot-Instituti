# Generated by Django 4.2.1 on 2023-06-12 09:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_remove_journalfilesurl_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsurl',
            name='related_words',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]