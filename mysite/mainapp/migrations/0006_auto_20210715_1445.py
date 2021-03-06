# Generated by Django 2.2.10 on 2021-07-15 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20210715_0834'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название категории')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='post_category',
            field=models.CharField(default='Рецептуры напитков', max_length=30, verbose_name='Категория'),
        ),
    ]
