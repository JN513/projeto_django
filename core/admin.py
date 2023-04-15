from django.contrib import admin
from core.models import PostModel


class PostAdmin(admin.ModelAdmin):
    list_display = ["titulo", "datetime", "user"]


admin.site.register(PostModel, PostAdmin)
