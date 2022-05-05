# Generated by Django 4.0.3 on 2022-05-04 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('captini', '0009_alter_flashcard_options_alter_prompt_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country_rank',
            field=models.IntegerField(default=0, verbose_name='country rank'),
        ),
        migrations.AddField(
            model_name='user',
            name='global_rank',
            field=models.IntegerField(default=0, verbose_name='global rank'),
        ),
        migrations.AddField(
            model_name='user',
            name='score',
            field=models.IntegerField(default=0, verbose_name='score'),
        ),
    ]
