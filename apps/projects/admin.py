from django.contrib import admin
from .models import Project, ProjectImage, ProjectDocument

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectDocumentInline(admin.TabularInline):
    model = ProjectDocument
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'ward', 'status', 'total_budget', 'updated_at')
    list_filter = ('status', 'ward__sub_county', 'ward')
    search_fields = ('name', 'description')
    inlines = [ProjectImageInline, ProjectDocumentInline]

    def total_budget(self, obj):
        from django.db.models import Sum
        return obj.budgets.aggregate(Sum('amount'))['amount__sum'] or 0
    total_budget.short_description = 'Total Budget'
