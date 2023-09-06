# Generated by Django 4.2.4 on 2023-09-06 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_alter_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]
