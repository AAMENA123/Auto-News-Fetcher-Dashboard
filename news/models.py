from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=500)
    summary = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=100)
    published_at = models.DateTimeField()
    url = models.URLField(max_length=500, blank=True, null=True,unique=True)
    url_to_image = models.URLField(max_length=500, blank=True, null=True)
    
    class Meta:
        ordering = ['-published_at']
    
    def __str__(self):
        return self.title