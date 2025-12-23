from django.db import models
from django.utils import timezone

class Zodiac(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  # default for existing rows
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Horoscope(models.Model):
    zodiac = models.ForeignKey(Zodiac, on_delete=models.CASCADE)
    date = models.DateField()
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.zodiac.name} - {self.date}"
