from django.db import models

class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f"{self.id}: {self.title}"