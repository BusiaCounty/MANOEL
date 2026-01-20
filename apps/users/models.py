from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    class Role(models.TextChoices):
        PUBLIC = 'PUBLIC', _('Public')
        STAFF = 'STAFF', _('Staff')
        EXECUTIVE = 'EXECUTIVE', _('Executive')

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.PUBLIC,
        help_text=_("User role in the system")
    )
    phone_number = models.CharField(max_length=15, blank=True)
    
    def is_staff_member(self):
        return self.role == self.Role.STAFF or self.is_staff

    def is_executive(self):
        return self.role == self.Role.EXECUTIVE
