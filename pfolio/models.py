from django.db import models

# Create your models here.

class Pfolio(models.Model):
     title = models.CharField(max_length=100)
     description = models.TextField(max_length=1000)
     image = models.ImageField(upload_to='pfolios')
     category = models.CharField(max_length=100,blank=True)
     views_count = models.IntegerField(default=0)

     def __str__(self):
         return self.title

class About(models.Model):
    introduction = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='abouts')
    clients = models.IntegerField(default=0)
    projects = models.IntegerField(default=0)
    collabs = models.IntegerField(default=0)

    def __str__(self):
         return self.introduction

class Contact(models.Model):
     name = models.CharField(max_length=30)
     email = models.EmailField(max_length=254)
     subject = models.CharField(max_length=100)
     message = models.CharField(max_length=200)

     def __str__(self):
         return self.name