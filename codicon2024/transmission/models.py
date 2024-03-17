from django.db import models
from accounts.models import CustomUser
from django.utils.crypto import get_random_string

class Categoria(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name
    
class Tags(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name
    
class Transmission(models.Model):
    """Transmission Model"""
    
    name = models.CharField(max_length=250,blank = False)
    creation_date = models.DateTimeField()
    transmission_start_date= models.DateTimeField()
    start_time= models.TimeField()
    end_time = models.TimeField()
    is_private = models.BooleanField(default= False)
    description = models.TextField()
    link = models.URLField(max_length=200, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='transmissions', null=True)
    tags = models.ManyToManyField(Tags, related_name='transmissions')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='transmissions', null=True)
    short_id = models.CharField(max_length=10, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.short_id:
            self.short_id = get_random_string(6)
        super().save(*args, **kwargs)