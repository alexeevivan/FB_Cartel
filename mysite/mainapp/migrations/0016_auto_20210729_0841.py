# Generated by Django 2.2.10 on 2021-07-29 08:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20210729_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
