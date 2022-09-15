from django.db import models

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class slider(models.Model):
    student_photo=models.ImageField(null=True,blank=True,upload_to="static/images/")
    title=models.CharField('title',max_length=120) 
    desscription=models.CharField('desscription',max_length=120) 
    def __str__(self):
       return self.title+'  '+self.desscription
class TeacherExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name




classes=[('ICT','ICT'),('HD','HD'),('TD','TD'),
('FB','FB')]
class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    roll = models.CharField(max_length=10)
    mobile = models.CharField(max_length=40,null=True)
    COURSE = models.CharField(max_length=40,null=True)
    ID_NUMBER = models.CharField(max_length=40,null=True)
    LEVEL = models.CharField(max_length=40,null=True)
    ACADEMIC_YEAR = models.CharField(max_length=40,null=True)
    RESIDENCE = models.CharField(max_length=40,null=True)
    TEL_NO = models.CharField(max_length=40,null=True)
    TEL_NO1 = models.CharField(max_length=40,null=True)
    fee=models.PositiveIntegerField(null=True)
    cl= models.CharField(max_length=10,choices=classes,default='one')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name



class Attendance(models.Model):
    roll=models.CharField(max_length=10,null=True)
    date=models.DateField()
    cl=models.CharField(max_length=10)
    present_status = models.CharField(max_length=10)



class Notice(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=20,null=True,default='school')
    message=models.CharField(max_length=500)

