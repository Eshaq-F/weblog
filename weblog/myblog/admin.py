from django.contrib import admin, messages
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *


class PostAdmin(admin.ModelAdmin):
    fields = ["title", "content", "image", "tag", "category", "author", "is_active",
              "is_confirmed", "like", "dislike", "pub_date"]
    list_filter = ['category', 'tag']
    readonly_fields = ['like', 'dislike', 'pub_date', 'category', 'author', 'image']
    list_display = ('title', 'author', 'pub_date', 'is_active', 'is_confirmed')
    actions = ['active_all_post', 'deactive_all_post']

    def change_view(self, request, object_id, form_url='', extra_context=None):
        author_group = Group.objects.get(name='نويسندگان')
        editor_group = Group.objects.get(name='ويراستاران')
        admin_group = Group.objects.get(name='مديران')
        if author_group in request.user.groups.all():
            self.fields.append('is_active')
            self.fields = list(dict.fromkeys(self.fields))
        elif editor_group in request.user.groups.all():
            self.fields.append('is_active')
            self.fields.append('is_confirmed')
            self.fields = list(dict.fromkeys(self.fields))
        elif admin_group in request.user.groups.all():
            self.fields.append('is_active')
            self.fields.append('is_confirmed')
            self.fields = list(dict.fromkeys(self.fields))

        return super().change_view(request, object_id, form_url, extra_context=None)

    def reset_questions(self, request, queryset):
        try:
            Post.objects.all().update(is_active=True)
            self.message_user(request, f'', messages.SUCCESS)
        except Exception:
            self.message_user(request, 'خطایی پیش آمد', messages.ERROR)

    def active_all_post(self, request, queryset):
        try:
            Post.objects.filter(pk__in=queryset).update(is_active=True)
            self.message_user(request, f'{queryset.count()} پست فعال شد.', messages.SUCCESS)
        except Exception:
            self.message_user(request, 'خطایی پیش آمد', messages.ERROR)

    def deactive_all_post(self, request, queryset):
        try:
            Post.objects.filter(pk__in=queryset).update(is_active=False)
            self.message_user(request, f'{queryset.count()} پست غير فعال شد.', messages.SUCCESS)
        except Exception:
            self.message_user(request, 'خطایی پیش آمد', messages.ERROR)

    active_all_post.short_description = 'فعال كردن همه'
    deactive_all_post.short_description = 'غير‌فعال كردن همه'

    def get_queryset(self, request):
        author_group = Group.objects.get(name='نويسندگان')
        editor_group = Group.objects.get(name='ويراستاران')
        admin_group = Group.objects.get(name='مديران')
        qs = super(PostAdmin, self).get_queryset(request)
        for i in [author_group, editor_group, admin_group]:
            if i in request.user.groups.all():
                return qs.filter(author=request.user)
            else:
                return qs


class CommentAdmin(admin.ModelAdmin):
    fields = ['content', 'post', 'like', 'dislike']
    readonly_fields = ['post', 'like', 'dislike']
    list_display = ('__str__', 'post', 'is_confirmed')

    def change_view(self, request, object_id, form_url='', extra_context=None):
        editor_group = Group.objects.get(name='ويراستاران')
        admin_group = Group.objects.get(name='مديران')
        if editor_group or admin_group in request.user.groups.all():
            self.fields.append('is_confirmed')
            self.fields = list(dict.fromkeys(self.fields))

        return super().change_view(request, object_id, form_url, extra_context=None)


class TagAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name', 'count_used',)
    Tag.count_used.short_description = 'دفعات استفاده'


class UserExtraInfoInline(admin.StackedInline):
    model = UserExtraInfo
    can_delete = False
    min_num = 1
    verbose_name_plural = 'اطلاعات اضافي'


class UserAdmin(BaseUserAdmin):
    inlines = [UserExtraInfoInline]


admin.site.register(Category)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(LikeCommentLog)
admin.site.register(LikePostLog)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
