from django.db import models

# Create your models here.
class Bangalore_jobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=40)
    title = models.CharField(max_length=30)
    address = models.CharField(max_length=20)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()

class Hydrabad_jobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=40)
    title = models.CharField(max_length=30)
    address = models.CharField(max_length=20)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()

class Bihar_jobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=40)
    title = models.CharField(max_length=30)
    address = models.CharField(max_length=20)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
