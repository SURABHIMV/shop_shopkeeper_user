from django.db import models

# Create your models here.
class shop(models.Model):
     shop_Name = models.CharField(max_length=100,null=True)

class shopkeeper(models.Model):
     shopkeeper_Name = models.CharField(max_length=100,null=True)

class shop_user(models.Model):
     user_Name = models.CharField(max_length=100,null=True)

class added_shopkeeper(models.Model):
     addedshopkeeper_Name = models.CharField(max_length=100,null=True)

class product(models.Model):
     product_Name = models.CharField(max_length=100,null=True)
     product_Quantity = models.CharField(max_length=100,null=True)
     

