# Generated by Django 2.2.10 on 2021-07-29 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_auto_20210729_0806'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='uploaded_image',
        ),
    ]