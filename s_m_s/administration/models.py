from django.db import models

# Create your models here.
class Designation(models.Model):
	name=models.CharField(max_length=15, unique=True)
	date=models.DateField(auto_now_add=True)

	def __str__(self):
		return self.name