from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(LikeCommentLog)
admin.site.register(LikePostLog)