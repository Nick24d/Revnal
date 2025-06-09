from django.contrib import admin
from .models import CodeReviewRequest, CodeAttachment

# Register your models here.
class CodeAttachmentInline(admin.TabularInline):
    model = CodeAttachment
    extra = 0


@admin.register(CodeReviewRequest)
class CodeReviewRequestAdmin(admin.ModelAdmin):
    list_display = ('sender_email', 'pr_url', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('sender_email', 'pr_url')
    inlines = [CodeAttachmentInline]
    ordering = ('-created_at',)

