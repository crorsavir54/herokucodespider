from django.db import models


class Room(models.Model):
	building = models.ForeignKey("Building", on_delete=models.CASCADE)
	display_number = models.PositiveSmallIntegerField()
	def __str__(self):
		return f'{self.building.name} - {self.display_number}'