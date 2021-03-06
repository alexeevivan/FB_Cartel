# Generated by Django 4.0 on 2021-12-16 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0032_auto_20211214_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostViews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IPAddres', models.GenericIPAddressField(default='127.0.0.1')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='IpModel',
        ),
        migrations.AddField(
            model_name='postviews',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.post'),
        ),
    ]
