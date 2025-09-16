from django.db import models

# Create your models here.

# campusApp/models.py
from django.db import models

# campusApp/models.py
from django.db import models


class UniversityCampus(models.Model):
    # The campus name, e.g. "North Campus"
    campus_name = models.CharField(max_length=100)

    # Two-letter state abbreviation, like "CA" or "NY"
    state = models.CharField(max_length=2)

    # Unique numeric ID for the campus
    campus_id = models.IntegerField(unique=True)

    # Default manager (included explicitly per assignment instructions)
    objects = models.Manager()

    class Meta:
        verbose_name = "University Campus"
        verbose_name_plural = "University Campuses"

    def __str__(self):
        return f"{self.campus_name} ({self.state})"
