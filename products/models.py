from django.db import models

class product(models.Model):
	product_image = models.ImageField(upload_to = 'product_image/')
	catagory = models.CharField(max_length = 20)
	title = models.CharField(max_length = 20)
	badge = models.CharField(max_length = 20)
	price = models.IntegerField()
