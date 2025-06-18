from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class lawyers(models.Model):
    name = models.CharField(max_length=100)
    def save(self, *args, **kwargs):
        if not self.pk and not self.name.startswith("Adv."):
            self.name = f"Adv. {self.name.strip()}"
        super().save(*args, **kwargs)
    GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
    ]

    gender = models.CharField(
    max_length=1,
    choices=GENDER_CHOICES,
    default='O',
    help_text="Select gender"
    )
    photo = models.ImageField(upload_to='photos/')
    cases_solved = models.CharField(
    max_length=50,
    default="New Here",
    help_text="Number of cases solved or default status"
    )
    LOCATION_CHOICES = [
    ('Delhi', 'Delhi'),
    ('Mumbai', 'Mumbai'),
    ('Bangalore', 'Bangalore'),
    ('Chennai', 'Chennai'),
    ('Kolkata', 'Kolkata'),
    ('Hyderabad', 'Hyderabad'),
    ('Pune', 'Pune'),
    ('Ahmedabad', 'Ahmedabad'),
    ('Jaipur', 'Jaipur'),
    ('Lucknow', 'Lucknow'),
    
    ]

    location = models.CharField(
    max_length=100,
    choices=LOCATION_CHOICES,
    default='Delhi',
    help_text="Select city where the lawyer is based"
    )
    
    experience = models.IntegerField(help_text="Years of experience")

    LANGUAGE_CHOICES = [
    ('EN', 'English'),
    ('HI', 'Hindi'),
    ('KA', 'Kannada'),
    ('MAL', 'Malayalam'),
    ('TA', 'Tamil'),
    ('TE', 'Telugu'),
    ]

    languages = MultiSelectField(choices=LANGUAGE_CHOICES)
    email = models.EmailField(unique=True)
    SPECIALIZATION_CHOICES = [
        ('CRIMINAL', 'Criminal'),
        ('CIVIL', 'Civil'),
        ('CORPORATE', 'Corporate (Business)'),
        ('CONSTITUTIONAL', 'Constitutional'),
        ('FAMILY', 'Family'),
    ]
    specialization = models.CharField(
        max_length=20,
        choices=SPECIALIZATION_CHOICES,
        default='CRIMINAL',
        help_text='Select one area of specialization'
    )
    bio = models.TextField(blank=True, help_text="Enter a short professional bio")
    age = models.IntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(100)],
        help_text="Enter age (must be between 18 and 100)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
# Create your models here.
