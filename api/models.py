from django.db import models

# Create your models here.
class Query(models.Model):
    cadaster_number = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'№ {self.cadaster_number}'
        

class Result(models.Model):
    query = models.OneToOneField(Query, on_delete=models.CASCADE)
    success = models.BooleanField()
    response_timestamp = models.DateTimeField(auto_now_add=True)