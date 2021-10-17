from django.db import models

# Create your models here.
class Login(models.Model):
    Username=models.CharField(max_length=30)
    Password=models.CharField(max_length=8)
class Article(models.Model):
    headline=models.CharField(max_length=100)
    publications=models.CharField(max_length=100)
class UserDetails(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    date=models.DateField()
    loginid=models.ForeignKey(Login,on_delete=models.CASCADE)
    place=models.CharField(max_length=30)
    parentname=models.CharField(max_length=30)
    phone=models.BigIntegerField()
class Profilepic(models.Model):
    profilepic=models.FileField(upload_to='profimages/')
    loginid=models.ForeignKey(Login,on_delete=models.CASCADE)
class AjaxUdetails(models.Model):
    name=models.CharField(max_length=30)
    contact=models.BigIntegerField()
    place=models.CharField(max_length=30)
