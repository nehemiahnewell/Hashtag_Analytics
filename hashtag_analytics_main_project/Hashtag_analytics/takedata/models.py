from django.db import models

# Create your models here.

# Transitory Analysis Table

class postData(models.Model):
    postID = models.BigIntegerField
    authorID = models.BigIntegerField

    postID.primary_key = True

class hashtags(models.Model):
    postID = models.ForeignKey(postData)
    hashtag = models.CharField(max_length=140)