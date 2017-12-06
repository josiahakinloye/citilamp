from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Post

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp"]
	list_filter = ["updated", "timestamp"]
	search_fields = ["title", "content"]
	exclude = ['slug',]