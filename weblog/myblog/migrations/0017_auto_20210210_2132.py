# Generated by Django 3.1.4 on 2021-02-10 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0016_auto_20210210_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name='تاريخ\u200c انتشار'),
        ),
    ]