from django.db import models
from django.db import models
from django.db.models import Manager
from django import forms
from datetime import datetime, timedelta
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class AdultParticipantManger(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            date_of_birth__lte=(datetime.now().date() - timedelta(days=365.25*18)),
            email__regex=r'^[a-zA-Z0-9._%+-]+@ur.ac.rw$',
            )
        
class Participants(models.Model):
    gender_choices = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Others"),
    ]
    phone_regex = RegexValidator(
        regex=r'^\+\d{12}$',
        message="Phone number must be entered in the format: '+123456789012'."
    )
    email_regex = RegexValidator(
        regex=r'^[a-zA-Z0-9._%+-]+@ur.ac.rw$',
        message="the email should be anything@ur.ac.rw",
        )
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank = True, null = True)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=13, validators=[phone_regex])
    gender = models.CharField(max_length=1, choices=gender_choices)
    email = models.EmailField(unique=True, validators=[email_regex])
    objects = models.Manager()
    adults = AdultParticipantManger()
    
    reference_number = models.IntegerField(
        validators=[
            MinValueValidator(99, message="Reference number must be at least 99."),
            MaxValueValidator(999, message="Reference number must be at most 999.")
        ], unique=True
    )

    # def is_valid_phone(self):
    #     """Check if the phone attribute is valid."""
    #     return bool(self.phone) and (self.phone[0]) == '+' and self.phone[1:].isdigit() and len(self.phone) == 13
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# vehicle starts here
class ManufactureDate(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            man_date__lte=(datetime.now().date() - timedelta(days=365.25*18)),
            email__regex=r'^[a-zA-Z0-9._%+-]+@ur.ac.rw$',
            )
        
class Vehicle(models.Model):
    def validate_manufact_year_2000(value):
        if value.year < 2000:
            raise ValidationError(_('Date must not be older than the year 2000.'))#change from valid error to message

    plate_regex = RegexValidator(
        regex=r'^(RA[A-H]\d{1,3}[A-Z]$|RNP\d{1,3}[A-Z]$|RDF\d{1,3}[A-Z])',
        message="Plate number must be entered in the correct format:'",
    ) 
    type_choices = [
        ("M", "Minivane"),
        ("S", "Sports car"),
        ("O", "others"),
    ]
    plate = models.CharField(unique=True, max_length=7, validators=[plate_regex])
    make = models.CharField(max_length=20)
    color = models.CharField(max_length=15)
    man_date = models.DateField(validators=[validate_manufact_year_2000])
    car_type = models.CharField(max_length=1, choices=type_choices)
    participant = models.ForeignKey(Participants, on_delete=models.CASCADE)  
    def __str__(self):
        return f"{self.participant}"

