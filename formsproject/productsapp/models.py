from django.db import models

# Create your models here.
class ProductModel(models.Model):
	no = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30,unique=True)
	price = models.FloatField()
	quantity = models.IntegerField()