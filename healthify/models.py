from django.db import models

# Create your models here.


DOCTOR_SPECIALIZATION_CHOICES = [
    ('Cardiologist', 'Cardiologist'),
    ('Dermatologist', 'Dermatologist'),
    ('Neurologist', 'Neurologist'),
    ('Pediatrician', 'Pediatrician'),
    ('Psychiatrist', 'Psychiatrist'),
    ('Radiologist', 'Radiologist'),
    ('Surgeon', 'Surgeon'),
    ('Orthopedic', 'Orthopedic'),
    ('Ophthalmologist', 'Ophthalmologist'),
    ('Gynecologist', 'Gynecologist'),
    ('Oncologist', 'Oncologist'),
    ('Anesthesiologist', 'Anesthesiologist'),
    ('Endocrinologist', 'Endocrinologist'),
    ('Gastroenterologist', 'Gastroenterologist'),
    ('Nephrologist', 'Nephrologist'),
    ('Rheumatologist', 'Rheumatologist'),
    ('Pulmonologist', 'Pulmonologist'),
    ('Urologist', 'Urologist'),
    ('Pathologist', 'Pathologist'),
    ('ENT Specialist', 'ENT Specialist')
]


BLOOD_GROUP_CHOICES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-')
    ]


GENDER = [
    ('Male','Male'),
    ('Female','Female'), 
    ('Others','Others')  
    ]

FOOD_TYPE = [
    ('Veg', 'Veg'), 
    ('Non_Veg', 'Non_Veg')
    ]


class UserDetails(models.Model):
    full_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(
        max_length=10,
        choices=GENDER
    )
    phone_number = models.IntegerField()
    current_medications = models.TextField()
    ALLERGIES = models.TextField()
    past_medical_condition = models.TextField()
    blood_type = models.CharField(
        max_length=5,
        choices=BLOOD_GROUP_CHOICES
    )
    recent_test_details = models.FileField(upload_to='user_details/')
    food_type = models.CharField(
        max_length=15,
        choices=FOOD_TYPE
    )
    address = models.TextField()


class DoctorDetails(models.Model):
    fullname = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10,choices=GENDER)
    blood_type = models.CharField(max_length=5,choices=BLOOD_GROUP_CHOICES)
    phone_number = models.IntegerField()
    adhaar_number = models.BigIntegerField()
    MIDICAL_LICENCE_NO = models.TextField()
    specialization = models.CharField(
        max_length=50,
        choices=DOCTOR_SPECIALIZATION_CHOICES
    )
    food_type = models.CharField(
        max_length=15,
        choices=FOOD_TYPE
    )
    years_of_experience = models.IntegerField()

class userRequestForDoctor(models.Model):
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField()
    specialization = models.CharField(
        max_length=50,
        choices=DOCTOR_SPECIALIZATION_CHOICES
    )



