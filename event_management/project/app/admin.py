from django.contrib import admin
from .models import Event, Registration, EventCategory

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'created_by')
    search_fields = ('title', 'description')
    list_filter = ('date',)

admin.site.register(Registration)
admin.site.register(EventCategory)
