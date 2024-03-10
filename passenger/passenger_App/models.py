from django.db import models

# Create your models here.
class passenger(models.Model):
    passenger_ID=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.PositiveBigIntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    mobile_number=models.CharField(max_length=100)
    booking_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    




