from django.db import models

# Create your models here.
class Image(models.Model):
	# add data type 
	name = models.CharField(max_length = 200)
	img = models.ImageField(null = True , blank = True )	
	def __str__(self):
		return self.name 
