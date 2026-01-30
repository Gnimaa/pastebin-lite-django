from django.db import models
import uuid

# Create your models here.
class Paste(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    views = models.IntegerField(default=0)
    max_views = models.IntegerField(null=True, blank=True)

    def is_expired(self):
        from django.utils import timezone
        if self.expires_at and timezone.now() > self.expires_at:
            return True
        if self.max_views is not None and self.views >= self.max_views:
            return True
        return False