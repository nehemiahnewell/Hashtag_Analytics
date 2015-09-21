from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

# Records Table

class searchData(models.Model):
    hashtag_searched = models.CharField(max_length=140)
    date_searched = models.DateTimeField('date published')

class hashtags(models.Model):
    search = models.ForeignKey(searchData)
    hashtag_found = models.CharField(max_length=140)
    Use_By_Count = models.IntegerField
    Use_By_Percentage = models.DecimalField(max_digits=4,decimal_places=2)
    Use_By_Posters = models.IntegerField
    Use_By_Percentage_Posters = models.DecimalField(max_digits=4,decimal_places=2)
