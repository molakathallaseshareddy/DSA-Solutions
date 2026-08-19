from django.db import models

# Create your models here.
class Cust(models.Model):
    cid = models.IntegerField(primary_key = True)
    cname = models.CharField(max_length = 20)
    busno = models.IntegerField(max_length = 6)