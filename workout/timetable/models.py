from django.db import models
from hashid_field import HashidAutoField


# Create your models here.
class TimeTableModel(models.Model):
    id = HashidAutoField(primary_key=True)
    name_workout = models.CharField(max_length=18, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True, db_index=True)
