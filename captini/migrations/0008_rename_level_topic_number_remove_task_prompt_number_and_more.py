# Generated by Django 4.0.3 on 2023-02-22 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('captini', '0007_rename_lesson_prompt_lesson'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='level',
            new_name='number',
        ),
        migrations.RemoveField(
            model_name='task',
            name='prompt_number',
        ),
        migrations.AddField(
            model_name='lesson',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='prompt',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='task',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
