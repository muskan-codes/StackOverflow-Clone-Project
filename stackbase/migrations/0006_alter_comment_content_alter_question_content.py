# Generated by Django 4.2 on 2023-04-18 09:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stackbase', '0005_question_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
