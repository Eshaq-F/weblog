# Generated by Django 3.1.4 on 2021-01-26 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='نام')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.category', verbose_name='سرشاخه')),
            ],
            options={
                'verbose_name': 'دسته\u200cبندي',
                'verbose_name_plural': 'دسته\u200cبندي\u200cها',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='متن نظر')),
                ('like', models.IntegerField(default=0, verbose_name='پسنديده')),
                ('dislike', models.IntegerField(default=0, verbose_name='نپسنديده')),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'نظرات',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('content', models.TextField(verbose_name='محتوا')),
                ('image', models.ImageField(upload_to='posts_img', verbose_name='تصوير')),
                ('tag', models.CharField(blank=True, max_length=2000, verbose_name='برچسب')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('is_confirmed', models.BooleanField(default=False, verbose_name='مجاز')),
                ('like', models.IntegerField(default=0, verbose_name='پسنديده')),
                ('dislike', models.IntegerField(default=0, verbose_name='نپسنديده')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاريخ\u200c انتشار')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نويسنده')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.category', verbose_name='دسته\u200cبندي')),
            ],
            options={
                'verbose_name': 'پست',
                'verbose_name_plural': 'پست ها',
            },
        ),
        migrations.CreateModel(
            name='LikePostLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_or_dislike', models.BooleanField(verbose_name='پسنديدن يا نپسنديدن')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='myblog.post', verbose_name='پست')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL, verbose_name='كاربر')),
            ],
            options={
                'verbose_name': 'گزارش پسنديدن يا نپسنديدن پست',
                'verbose_name_plural': 'گزارشات پسنديدن يا نپسنديدن پست\u200cها',
            },
        ),
        migrations.CreateModel(
            name='LikeCommentLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_or_dislike', models.BooleanField(verbose_name='پسنديدن يا نپسنديدن')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='myblog.comment', verbose_name='نظر')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL, verbose_name='كاربر')),
            ],
            options={
                'verbose_name': 'گزارش پسنديدن يا نپسنديدن نظر',
                'verbose_name_plural': 'گزارشات پسنديدن يا نپسنديدن نظرات',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.post', verbose_name='پست'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='كاربر'),
        ),
    ]
