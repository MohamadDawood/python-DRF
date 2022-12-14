from django.db import models


# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=30)
    is_available = models.BooleanField(default=True)
    owner = models.CharField(max_length=30, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
