from django.contrib import admin
from website.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'create_date']
    list_filter = ['email']
    search_fields = ['name', 'message']
    date_hierarchy = 'create_date'

    class Meta:
        ordering = ['create_date']
        
admin.site.register(Contact, ContactAdmin)
