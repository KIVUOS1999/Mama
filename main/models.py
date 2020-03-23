from django.db import models


class column(models.Model):
    name = models.CharField(max_length = 200)
    length = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class row(models.Model):
    available_lengths = models.IntegerField()
