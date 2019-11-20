from django.db import models

class product(models.Model):
	product_image = models.ImageField(upload_to = 'product_image/')
	catagory = models.CharField(max_length = 100)
	title = models.CharField(max_length = 50)
	color = models.CharField(max_length = 50)
	badge = models.CharField(max_length = 100, blank=True, null=True)
	price = models.IntegerField()
