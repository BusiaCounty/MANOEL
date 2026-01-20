from django.contrib import admin
from .models import SubCounty, Ward

@admin.register(SubCounty)
class SubCountyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')

@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ('name', 'sub_county', 'code')
    list_filter = ('sub_county',)
    search_fields = ('name', 'code')
