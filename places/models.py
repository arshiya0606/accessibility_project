from django.db import models
from django.db.models import Avg

class Place(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    has_ramp = models.BooleanField(default=False)
    has_elevator = models.BooleanField(default=False)
    has_accessible_toilet = models.BooleanField(default=False)

    average_rating = models.FloatField(default=0)

    #def accessibility_score(self):
     #   return int(self.has_ramp) + int(self.has_elevator) + int(self.has_accessible_toilet)

    def update_average_rating(self):
        avg = self.ratings.aggregate(Avg('rating'))['rating__avg']
        self.average_rating = avg if avg else 0
        self.save()

    def __str__(self):
        return self.name


class Rating(models.Model):
    place = models.ForeignKey(
        Place,
        related_name='ratings',
        on_delete=models.CASCADE
    )
    rating = models.IntegerField()
    comment = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.place.update_average_rating()