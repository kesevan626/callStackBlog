# Generated by Django 4.0.1 on 2022-01-23 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theBlog', '0011_remove_room_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
