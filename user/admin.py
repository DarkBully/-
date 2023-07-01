from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'description', 'creation_date')
    list_display_links = ('id', 'image')
    search_fields = ('id', 'image', 'description', 'creation_date')


admin.site.register(Post, PostAdmin)