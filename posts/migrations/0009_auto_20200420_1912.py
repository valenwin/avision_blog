# Generated by Django 3.0.5 on 2020-04-20 19:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20200420_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
