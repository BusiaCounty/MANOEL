from django.db import models
from apps.projects.models import Project
from django.conf import settings

class ProjectFeedback(models.Model):
    project = models.ForeignKey(Project, related_name='feedback', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, help_text="Null for anonymous")
    name = models.CharField(max_length=100, blank=True, help_text="Name if anonymous")
    email = models.EmailField(blank=True)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)], null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True, help_text="Visible to public")

    def __str__(self):
        return f"Feedback on {self.project.name}"
