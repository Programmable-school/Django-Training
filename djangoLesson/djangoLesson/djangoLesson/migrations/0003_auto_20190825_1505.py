# Generated by Django 2.2.4 on 2019-08-25 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoLesson', '0002_auto_20190825_1502'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diary',
            old_name='description',
            new_name='content',
        ),
    ]