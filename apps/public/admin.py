from django.contrib import admin
from .models import ProjectFeedback

@admin.register(ProjectFeedback)
class ProjectFeedbackAdmin(admin.ModelAdmin):
    list_display = ('project', 'user', 'rating', 'created_at', 'is_public')
    list_filter = ('is_public', 'rating', 'created_at')
    search_fields = ('project__name', 'content')
