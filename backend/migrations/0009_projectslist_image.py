# Generated by Django 4.2.1 on 2023-06-08 11:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_projectname_projectslist_delete_anoncurl_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectslist',
            name='image',
            field=models.FileField(default=django.utils.timezone.now, upload_to='projectImage/'),
            preserve_default=False,
        ),
    ]
