# Generated by Django 4.0 on 2021-12-16 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0034_alter_postviews_ipaddres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
    ]
