from django.db import models


class Employee(models.Model):

   name = models.CharField(max_length = 50)
   mail = models.CharField(max_length = 50)
   designation = models.CharField(max_length = 50)
   phonenumber = models.IntegerField()

   class Meta:
      db_table = "Employee_details"


class Article(models.Model):

   title = models.CharField(max_length = 50)
   auther = models.CharField(max_length = 50)
   cost = models.IntegerField()

   class Meta:
      db_table = "Article"
