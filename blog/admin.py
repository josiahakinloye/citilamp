from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]
    exclude = ['slug']
