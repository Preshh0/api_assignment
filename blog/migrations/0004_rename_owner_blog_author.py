# Generated by Django 4.0.1 on 2022-01-21 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blog_author_blog_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='owner',
            new_name='author',
        ),
    ]
