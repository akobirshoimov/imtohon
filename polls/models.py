from django.db import models
from datetime import datetime

# Create your models here.
class KitoblarModel(models.Model):
    name = models.CharField(max_length=100,default=' ')
    page = models.SmallIntegerField()
    pub_date = models.DateTimeField(default=datetime.now)
    
    
    def __str__(self) -> str:
        return self.name

class AvtorlarModel(models.Model):
    first_name = models.CharField(max_length=50,default=' ')
    last_name = models.CharField(max_length=60,default=' ')
    date_fo_birth = models.DateTimeField(default=datetime.now)
    combine = models.ForeignKey(KitoblarModel,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.first_name
    

    