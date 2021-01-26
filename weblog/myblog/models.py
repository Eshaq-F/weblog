from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name = 'دسته‌بندي'
        verbose_name_plural = 'دسته‌بندي‌ها'

    name = models.CharField('نام', max_length=30, unique=True)
    parent = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name='سرشاخه')

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    title = models.CharField('عنوان', max_length=50)
    content = models.TextField('محتوا')
    image = models.ImageField('تصوير', upload_to='posts_img')
    tag = models.CharField('برچسب', max_length=2000, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته‌بندي')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نويسنده')
    is_active = models.BooleanField('فعال', default=True)
    is_confirmed = models.BooleanField('مجاز', default=False)
    like = models.IntegerField('پسنديده', default=0)
    dislike = models.IntegerField('نپسنديده', default=0)
    pub_date = models.DateTimeField('تاريخ‌ انتشار', default=now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    content = models.TextField('متن نظر')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='پست')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='كاربر')
    like = models.IntegerField('پسنديده', default=0)
    dislike = models.IntegerField('نپسنديده', default=0)

    def __str__(self):
        return f'نظر كاربر {self.user}'


class LikeCommentLog(models.Model):
    class Meta:
        verbose_name = 'گزارش پسنديدن يا نپسنديدن نظر'
        verbose_name_plural = 'گزارشات پسنديدن يا نپسنديدن نظرات'

    comment = models.ForeignKey(Comment, on_delete=models.RESTRICT, verbose_name='نظر')
    user = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name='كاربر')
    # Like = True and Dislike = False
    like_or_dislike = models.BooleanField('پسنديدن يا نپسنديدن')

    def __str__(self):
        if self.like_or_dislike:
            return f'{self.user} پسنديده'
        else:
            return f'{self.user} نپسنديده'


class LikePostLog(models.Model):
    class Meta:
        verbose_name = 'گزارش پسنديدن يا نپسنديدن پست'
        verbose_name_plural = 'گزارشات پسنديدن يا نپسنديدن پست‌ها'

    post = models.ForeignKey(Post, on_delete=models.RESTRICT, verbose_name='پست')
    user = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name='كاربر')
    # Like = True and Dislike = False
    like_or_dislike = models.BooleanField('پسنديدن يا نپسنديدن')

    def __str__(self):
        if self.like_or_dislike:
            return f'{self.user} پسنديده'
        else:
            return f'{self.user} نپسنديده'
