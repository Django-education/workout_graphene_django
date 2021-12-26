from django.db import models


class Workout(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    place = models.TextField(max_length=150)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.title)


class Tag(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title