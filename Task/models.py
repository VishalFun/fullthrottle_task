from djongo import models
from datetime import datetime

class User(models.Model):
    real_name = models.CharField(max_length=50)
    tz = models.CharField(max_length=50)

    def __str__(self):
        return self.real_name

class ActivityPeriod(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='activity_periods')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()




