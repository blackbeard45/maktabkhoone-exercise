from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    empty_value_display = '-empty-'
    list_display = ['title', 'view_count', 'status', 'published_date', 'create_date']
    list_filter = ['status']
    # ordering = ['create_date']
    search_fields = ['title', 'content']


admin.site.register(Post, PostAdmin)
