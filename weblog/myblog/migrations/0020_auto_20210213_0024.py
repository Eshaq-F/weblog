# Generated by Django 3.1.4 on 2021-02-12 20:54

from django.db import migrations, models
import myblog.validators


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0019_auto_20210213_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=30, validators=[myblog.validators.check_tag]),
        ),
    ]