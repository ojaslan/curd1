
from django.db import models

class health(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)  # You might want to consider using a more secure method for storing passwords
    dob = models.DateField()
    contact = models.CharField(max_length=20)  # Assuming contact number is a string
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
      # Automatically set the sign-up date
    signupdate = models.DateField()


    def __str__(self):
        return self.name
