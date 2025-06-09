from django.contrib import admin
from .models import JournalEntry

# Register your models here.
@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ('sender_email', 'created_at', 'short_preview')
    list_filter = ('created_at',)
    search_fields = ('sender_email',)
    ordering = ('-created_at',)

    def short_preview(self, obj):
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
    short_preview.short_description = 'Preview'