from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.locations.models import Ward
from django.conf import settings

class Project(models.Model):
    class Status(models.TextChoices):
        PLANNED = 'PLANNED', _('Planned')
        TENDERING = 'TENDERING', _('Tendering')
        IN_PROGRESS = 'IN_PROGRESS', _('In Progress')
        STALLED = 'STALLED', _('Stalled')
        COMPLETED = 'COMPLETED', _('Completed')
        COMMISSIONED = 'COMMISSIONED', _('Commissioned')

    name = models.CharField(max_length=255)
    description = models.TextField()
    ward = models.ForeignKey(Ward, on_delete=models.SET_NULL, null=True, related_name='projects')
    location_details = models.CharField(max_length=255, blank=True, help_text="Specific location details")
    
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PLANNED)
    
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    
    contractor_name = models.CharField(max_length=255, blank=True)
    department = models.CharField(max_length=100, help_text="Department responsible")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='created_projects')

    def __str__(self):
        return self.name

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class ProjectDocument(models.Model):
    project = models.ForeignKey(Project, related_name='documents', on_delete=models.CASCADE)
    file = models.FileField(upload_to='project_docs/')
    title = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
