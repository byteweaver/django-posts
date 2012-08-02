from django.contrib import admin
from django.contrib.auth.models import User

from models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('headline', 'author', 'creation_date')

    def save_model(self, request, obj, form, change):
        try:
            obj.author
        except User.DoesNotExist:
            obj.author = request.user
        obj.save()

admin.site.register(Post, PostAdmin)
