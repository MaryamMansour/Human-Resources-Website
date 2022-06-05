from django.db import models

# Create your models here.
class Employee(models.Model):
    ID = models.IntegerField(primary_key=True)
    name = models.CharField (max_length=100)
    mail = models.CharField (max_length=100, unique= True)
    phoneNum = models.CharField (max_length=15)
    dateofBirth = models.DateField ()
    address= models.CharField (max_length=200)
    GENDER_CHOICES = (
        ('Male','Male'),
        ('Female','Female'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    MARITALSTATUS_CHOICES = (
         ('Single','Single'),
         ('Married','Married'),
     )
    maritalstatus = models.CharField(max_length=7, choices=MARITALSTATUS_CHOICES)
    availablevac = models.IntegerField ()
    approvedvac = models.IntegerField ()
    salary = models.IntegerField ()
    def __str__(self):
        return str(self.ID)

class Vacation(models.Model):
    employee = models.ForeignKey("Employee",on_delete=models.CASCADE,null = True)
    name = models.CharField(max_length = 100,null=True)
    vacStart = models.DateField(null = True)
    vacEnd = models.DateField(null = True)
    reason = models.CharField(max_length = 200)
    status = models.BooleanField(blank=True,null=True)
    def __int__(self):
        return self.ID


class Training(models.Model):
    name = models.CharField(max_length = 60,default='Training')
    available = models.BooleanField(default=True)
    taken = models.BooleanField(default=False)
    def __str__(self):
        return self.name


class OfficialHoliday(models.Model):
    name = models.CharField(max_length = 60,default='Official Holiday')
    coming_up = models.BooleanField(default=True)
    taken = models.BooleanField(default=False)
    planned = models.BooleanField(default=True)
    def __str__(self):
        return self.name


class importantMeeting(models.Model):
    MeetingID = models.IntegerField(default = '000')
    declared = models.BooleanField(default=True)
    planned = models.BooleanField(default=True)
    taken = models.BooleanField(default=False)
    def __str__(self):
        return str(self.MeetingID)
    
