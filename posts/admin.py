from django.contrib import admin
from django.contrib.auth import get_user_model

from models import Post


class AbstractPostAdmin(admin.ModelAdmin):
    list_display = ('headline', 'author', 'creation_date')

    def save_model(self, request, obj, form, change):
        try:
            obj.author
        except get_user_model().DoesNotExist:
            obj.author = request.user
        obj.save()


class PostAdmin(AbstractPostAdmin):
    prepopulated_fields = {"slug": ("headline",)}


admin.site.register(Post, PostAdmin)
