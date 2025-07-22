from django.db import models
from django.utils import timezone

class RateLimit(models.Model):
    ip_address = models.GenericIPAddressField()
    endpoint = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.ip_address} accessed {self.endpoint} at {self.timestamp}"
