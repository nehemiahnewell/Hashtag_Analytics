from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

# Records Table

class searchData(models.Model):
    hashtag_searched = models.CharField(max_length=140)
    date_searched = models.DateTimeField('date published')
    Tweets = models.IntegerField()

class hashtags(models.Model):
    search = models.ForeignKey(searchData)
    hashtag_found = models.CharField(max_length=140)
    Count = models.IntegerField()
    Percentage = models.DecimalField(max_digits=4,decimal_places=2)
    Posters = models.IntegerField()
    Percentage_Posters = models.DecimalField(max_digits=4,decimal_places=2)
