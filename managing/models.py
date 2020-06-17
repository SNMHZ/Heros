from django.db import models
class Notice(models.Model):
    title       = models.CharField(max_length=120)
    text        = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


class FAQ(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
#FAQ, Notice 틀 설정

