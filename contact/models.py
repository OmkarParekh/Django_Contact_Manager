from django.db import models

# Create your models here
class Contact(models.Model):
     Name = models.CharField(max_length=200)
     email=models.EmailField(max_length=140,null=True)
     Number = models.CharField(max_length=200)
   
 


    

