from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255, default="Untitled")  # Fix: Add max_length to CharField
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created']  # Orders by created_at, most recent first
    def __str__(self):
        return self.title  # Will return the title string correctly
