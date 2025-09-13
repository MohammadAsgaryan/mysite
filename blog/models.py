from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    
    counted_views = models.IntegerField(default=0) 
    status = models.BooleanField(default=False)
    published_date = models.DateField(null=True)
    crreated_at = models.DateTimeField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    
    
    