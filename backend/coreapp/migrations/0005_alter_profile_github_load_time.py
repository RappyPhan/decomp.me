# Generated by Django 3.2.6 on 2021-08-27 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0004_auto_20210827_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='github_load_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
