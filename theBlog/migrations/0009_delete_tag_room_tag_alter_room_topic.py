# Generated by Django 4.0.1 on 2022-01-23 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theBlog', '0008_alter_post_options_remove_categories_title_room'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AddField(
            model_name='room',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='theBlog.categories'),
        ),
        migrations.AlterField(
            model_name='room',
            name='topic',
            field=models.CharField(max_length=300),
        ),
    ]
