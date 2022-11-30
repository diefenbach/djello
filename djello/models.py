from django.db import models


class List(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Card(models.Model):
    title = models.CharField(max_length=50)
    list = models.ForeignKey(List, related_name="cards", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
