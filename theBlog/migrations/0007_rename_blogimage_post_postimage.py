# Generated by Django 4.0.1 on 2022-01-23 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theBlog', '0006_post_blogimage_alter_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='blogImage',
            new_name='postImage',
        ),
    ]
