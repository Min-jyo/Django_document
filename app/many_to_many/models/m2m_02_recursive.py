from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    similar_projects = models.ManyToManyField('self')

    def __str__(self):
        return self.name

