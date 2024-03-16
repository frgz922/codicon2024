from django.db import models
from accounts.models import CustomUser

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
    
    def _str_(self) -> str:
        return f" {self.name} {self.creation_date} "