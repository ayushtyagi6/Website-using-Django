from django.db import models
from django.utils import timezone
# Create your models here.
class Posts(models.Model):
    sno=models.AutoField(primary_key=True,auto_created=True)
    title=models.CharField(max_length=50)
    content=models.TextField()
    date=models.DateTimeField()
    slug=models.CharField(unique=True,max_length=50)
    name=models.CharField(max_length=50)
    applicable=models.CharField(max_length=50)
    likes=models.IntegerField()
    dislikes=models.IntegerField()