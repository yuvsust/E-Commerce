from django.conf import settings
from django.db import models

class product(models.Model):
	CATAGORY_CHOICES = (
		('S', 'Shirt'),
		('TS', 'T-Shirt'),
		('FS', 'Full Sleeve T-Shirt'),
		('H', 'Hoodie'),
		('PJ', 'Panjabi'),
		('PL', 'Polo'),
	)
	COLOR_CATAGORY = (
		('B', 'Black'),
		('W', 'White'),
		('N', 'Navy Blue'),
		('R', 'Red'),
		('M', 'Meroon')
	)
	BADGE_CATAGORY = (
		('NW', 'NEW'),
		('BS', 'Best Seller')
	)
	product_image = models.ImageField(upload_to = 'product_image/')
	catagory = models.CharField(choices=CATAGORY_CHOICES, max_length=50)
	title = models.CharField(max_length = 100)
	color = models.CharField(choices=COLOR_CATAGORY, max_length = 20)
	badge = models.CharField(choices=BADGE_CATAGORY, max_length = 20, blank=True, null=True)
	price = models.IntegerField()

	def __str__(self):
		return self.title
