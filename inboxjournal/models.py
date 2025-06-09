from django.db import models


# Create your models here.


class JournalEntry(models.Model):
    sender_email = models.EmailField(max_length=100, blank=False, null=False, db_index=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    pin = models.CharField(max_length=6, blank=True, null=True)

    @property
    def is_private(self):
        return self.pin is not None

    def __str__(self):
        return f"{self.sender_email} - {self.created_at.date()}"
