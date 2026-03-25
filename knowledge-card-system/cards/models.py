from django.db import models

# Create your models here.
class KnowledgeCard(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField()
    histogram = models.TextField()

    def __str__(self):
        return self.title