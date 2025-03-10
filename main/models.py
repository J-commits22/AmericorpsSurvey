from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email
    
class Student(models.Model):
    fname = models.CharField(max_length=100)
    email = models.EmailField(default='example@example.com')
    phone_num = models.IntegerField(default='xxx-xxx-xxxx')
    dob = models.DateField()
    student_id = models.IntegerField(default='xxxxxxx', primary_key = True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='Other')
    Str_add = models.CharField(max_length=200, default='Street Name')
    Str_add = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=50, default='Brownsville')
    postal_code = models.IntegerField(default='785xx')
    state = models.CharField(max_length=50, default='Texas')
    QUESTION1_CHOICES = (
        ('E', 'Elementary'),
        ('J', 'Jr. High School/Middle School'),
        ('H', 'High School'),
        ('S', 'Some College'),
        ('C', 'College Degree'),
        ('U', 'Unknown')
    )
    question1 = models.CharField(max_length=1, choices=QUESTION1_CHOICES)
    QUESTION2_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    question2 = models.CharField(max_length=1, choices=QUESTION2_CHOICES)
    QUESTION3_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    question3 = models.CharField(max_length=1, choices=QUESTION3_CHOICES)
    QUESTION4_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    question4 = models.CharField(max_length=1, choices=QUESTION4_CHOICES)
    GPA = models.DecimalField(max_digits=4, decimal_places=2)
    QUESTION6_CHOICES = (
        ('C', 'Plan on going to college'),
        ('N', 'Not going to college'),
        ('M', 'Plan to enroll in military'),
        ('W', 'Plan to work'),
        ('O', 'Other')
    )
    question6 = models.CharField(max_length=1, choices=QUESTION6_CHOICES)
    first_choice = models.CharField(max_length=200)
    second_choice = models.CharField(max_length=200)
    QUESTION9_CHOICES = (
        ('C', 'Certificate'),
        ('A', 'Associate'),
        ('B', 'Bachelors'),
        ('M', 'Military'),
        ('O', 'Other')
    )
    question9 = models.CharField(max_length=1, choices=QUESTION9_CHOICES)
    QUESTION10_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    question10 = models.CharField(max_length=1, choices=QUESTION10_CHOICES)
    QUESTION11_CHOICES = (
        ('P', 'Pending'),
        ('A', 'Accepted')
    )
    question11 = models.CharField(max_length=1, choices=QUESTION11_CHOICES)
    QUESTION12_CHOICES = (
        ('N', 'Not Testing'),
        ('R', 'Registered'),
        ('T', 'Tested')
    )
    question12 = models.CharField(max_length=1, choices=QUESTION12_CHOICES)
    QUESTION13_CHOICES = (
        ('S', 'SAT'),
        ('A', 'ACT'),
        ('N', 'N/A')
    )
    question13 = models.CharField(max_length=1, choices=QUESTION13_CHOICES)
    test_date = models.DateField()
    QUESTION15_CHOICES = (
        ('S', 'Sent'),
        ('P', 'Pending')
    )
    question15 = models.CharField(max_length=1, choices=QUESTION15_CHOICES)
    QUESTION16_CHOICES = (
        ('S', 'Sent'),
        ('P', 'Pending')
    )
    question16 = models.CharField(max_length=1, choices=QUESTION16_CHOICES)
    QUESTION17_CHOICES = (
        ('T', 'Tested-Pass'),
        ('F', 'Tested-Fail'),
        ('P', 'Pending')
    )
    question17 = models.CharField(max_length=1, choices=QUESTION17_CHOICES)
    QUESTION18_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    question18 = models.CharField(max_length=1, choices=QUESTION18_CHOICES)
    QUESTION19_CHOICES = (
        ('F', 'FAFSA'),
        ('T', 'TAFSA'),
        ('O', 'Other')
    )
    question19 = models.CharField(max_length=1, choices=QUESTION19_CHOICES)
    QUESTION20_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    question20 = models.CharField(max_length=1, choices=QUESTION20_CHOICES)
    appliedforAid = models.DateField()

    def __str__(self):
        return self.student_id + " " + self.fname


    '''
    GENDER_CHOICES = (
        ('M', 'Male')
        ('F', 'Female')
        ('O', 'Other')
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

        email = models.EmailField()
    phone_num = models.CharField(max_length=15)
    dob = models.DateField()
    student_id = models.CharField(max_length=50)
    Str_add = models.CharField(max_length=200)
    Str_adr2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    '''