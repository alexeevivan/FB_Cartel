# Generated by Django 2.2.10 on 2021-07-21 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20210721_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='short_description',
            field=models.CharField(default='Краткое описание поста', max_length=50, verbose_name='Краткое описание поста'),
        ),
    ]