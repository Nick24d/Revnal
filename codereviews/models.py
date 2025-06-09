from django.db import models


# Create your models here.
class CodeReviewRequest(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_COMPLETED = 'completed'

    STATUS_CHOICES = [(STATUS_PENDING, 'Pending'), (STATUS_IN_PROGRESS, 'In Progress'),
                      (STATUS_COMPLETED, 'Completed'), ]
    sender_email = models.EmailField(max_length=100, blank=False, null=False, db_index=True)
    pr_url = models.URLField(max_length=200)
    description = models.TextField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING, )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return f"{self.pr_url} + {self.status}"

class CodeAttachment(models.Model):
    code_review = models.ForeignKey(CodeReviewRequest, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)