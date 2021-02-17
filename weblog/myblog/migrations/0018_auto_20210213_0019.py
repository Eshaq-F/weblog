# Generated by Django 3.1.4 on 2021-02-12 20:49

from django.db import migrations, models
import myblog.validators


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0017_auto_20210210_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='name',
        ),
        migrations.AddField(
            model_name='tag',
            name='label',
            field=models.CharField(default='#', max_length=30, validators=[myblog.validators.check_tag]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(help_text='برچسب ها با# آغاز مي\u200cشوند و فقط شامل حروف الفبا و _ مي\u200cشوند. برچسب\u200cها را با فاصله از هم جدا كنيد', to='myblog.Tag', verbose_name='برچسب'),
        ),
    ]
