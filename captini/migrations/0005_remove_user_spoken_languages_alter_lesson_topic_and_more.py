# Generated by Django 4.0.3 on 2022-04-13 13:54

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('captini', '0004_flashcard_text_alter_user_spoken_languages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='spoken_languages',
        ),
        migrations.AlterField(
            model_name='lesson',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='captini.topic'),
        ),
        migrations.AlterField(
            model_name='user',
            name='progress',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True), size=None),
        ),
    ]