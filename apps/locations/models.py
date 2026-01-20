from django.db import models

class SubCounty(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Sub Counties"

    def __str__(self):
        return self.name

class Ward(models.Model):
    sub_county = models.ForeignKey(SubCounty, related_name='wards', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True, blank=True, null=True)

    class Meta:
        unique_together = ('sub_county', 'name')

    def __str__(self):
        return f"{self.name} ({self.sub_county.name})"
