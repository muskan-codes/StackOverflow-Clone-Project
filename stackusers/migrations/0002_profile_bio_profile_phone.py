# Generated by Django 4.2 on 2023-04-12 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackusers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
