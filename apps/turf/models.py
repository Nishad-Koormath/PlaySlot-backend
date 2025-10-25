from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Turf(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='turfs')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    day_price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    night_price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    day_start_time = models.TimeField(default="06:00")
    night_start_time = models.TimeField(default='18:00')
    is_active = models.BooleanField(default=True)
    craeted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class TurfImage(models.Model):
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='turfs/')
        
    def __str__(self):
        return f"Image for {self.turf.name}"
    
