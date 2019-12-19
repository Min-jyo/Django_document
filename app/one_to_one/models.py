from django.db import models


# Create your models here.

class Place(models.Model):
    address = models.CharField('주소', max_length=200)

    def __str__(self):
        return f'Place (address: {self.address})'


class Restuarant(models.Model):
    place = models.OneToOneField(Place, verbose_name='장소', on_delete=models.CASCADE)
    name = models.CharField('식당명', max_length=30)
    rating = models.IntegerField('평점', default=0)

    def __str__(self):
        return f'{self.name} (평점: {self.rating})'
