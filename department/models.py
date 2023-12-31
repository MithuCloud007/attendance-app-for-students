from django.db import models

# Create your models here.
class Department(models.Model):
    STATUS_OPTIONS = (('active','active'),('inactive','inactive'))
    status = models.CharField(max_length=255,choices=STATUS_OPTIONS,default='active')
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
             