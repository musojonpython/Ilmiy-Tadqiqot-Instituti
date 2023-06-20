# Generated by Django 4.2.1 on 2023-06-19 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_journalfilesurl_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='journalfilesurl',
            name='type_of_journal',
            field=models.CharField(choices=[('PDF', 'Kitoblar'), ('DOC', 'Wordlar'), ('JPG', 'Rasmlar')], default='PDF', max_length=3),
        ),
    ]