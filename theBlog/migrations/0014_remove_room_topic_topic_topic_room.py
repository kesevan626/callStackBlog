# Generated by Django 4.0.1 on 2022-01-23 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theBlog', '0013_topic_alter_room_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='topic',
        ),
        migrations.AddField(
            model_name='topic',
            name='topic_room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='theBlog.room'),
        ),
    ]
