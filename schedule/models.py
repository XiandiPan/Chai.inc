from django.db import models
# from datetime import timezone

class Employee(models.Model):

    # class Shifts(models.TextChoices):
    #     MONDAY_AM = 'MO-AM', 'Monday AM'
    #     MONDAY_PM = 'MO-PM', 'Monday PM'
    #     TUESDAY_AM = 'TU-AM', 'Tuesday AM'
    #     TUESDAY_PM = 'TU-PM', 'Tuesday PM'

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # availability = models.CharField(max_length=5,
    #                           choices=Shifts.choices,
    #                           default=Shifts.MONDAY_AM)
