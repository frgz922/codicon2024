from django.db import models

class Transmission(models.Model):
    """Transmission Model"""
    
    name = models.CharField(
        min_length=10, 
        max_length=250,
        blank = False
    )

    creation_date = models.DateTimeField(
        auto_now_add=True
    )
    
    transmission_start_date= models.DateTimeField(
        auto_now=True
    )
    
    start_time= models.TimeField(
        auto_now_add=True
    )
    
    end_time = models.TimeField(
        auto_now_add=True
    )
    
    is_private = models.BooleanField(
        default= False
    )
    
    description = models.TextField()
    
    def _str_(self) -> str:
        return f" {self.name} {self.creation_date} "
