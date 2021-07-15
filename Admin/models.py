from django.db import models
import random
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):

    USER_TYPES = [
        ('Manager', 'Manager'),
        ('Admin', 'Admin'),
        ('Employee', 'Employee'),
        ('HR', 'HR')
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profilePicture = models.ImageField(blank=True, null=True)
    contact_No = models.IntegerField()
    dob = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    userType = models.CharField(max_length=15, choices=USER_TYPES, default='Employee')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username


class OTP(models.Model):
    def Get_OTP():
        return random.randint(100000, 999999)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.IntegerField(default=Get_OTP)
    created_at = models.DateTimeField(auto_now_add=True)


class Attendance(models.Model):

    STATUS = [
        ('Absent', 'Absent'),
        ('Present', 'Present')        
    ]
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField()
    in_time = models.TimeField()
    out_time = models.TimeField()
    status = models.CharField(max_length=15, choices=STATUS, default='Present')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.user.userType


class Timesheet(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name= models.CharField(max_length=30,null=True,blank=True)
    contact_No = models.IntegerField()
    date = models.DateField(null=True,blank=True)
    status = models.CharField(max_length=20,null=True,blank=True)
    task= models.CharField(max_length=50,null=True,blank=True)
    assignby= models.CharField(max_length=30,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.user.userType

class Leaveapplication(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    )
    def GenID():
        return random.randint(10000000000, 99999999999)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    leaveType = models.CharField(max_length=30)
    reasons= models.CharField(max_length=300,null=True,blank=True)
    leave_id = models.CharField(max_length=30, default=f'LA{GenID()}')
    status = models.CharField(max_length=20, choices=STATUS, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return "User " +self.user.user.username + "has applied leave application from " + str(self.from_date) + " to " + str(self.to_date) 


class AddEvent(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField(null=True,blank=True)
    ename = models.CharField(max_length=30,null=True,blank=True)
    venue= models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.user.userType

class RecruitNotice(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=30,null=True,blank=True)
    description= models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.user.userType


class ResultPublish(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField(null=True,blank=True)
    ename = models.CharField(max_length=30,null=True,blank=True)
    description= models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.user.userType

class Interview(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected')
    )
    def GenID():
        return random.randint(10000000000, 99999999999)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    candidate_name = models.CharField(max_length=255,null=True,blank=True)
    candidate_email = models.CharField(max_length=100)
    candidate_description = models.TextField()  
    feedback= models.CharField(max_length=255,null=True,blank=True)
    interview_id = models.CharField(max_length=30, default=f'IN{GenID()}')
    status = models.CharField(max_length=20, choices=STATUS, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.user.userType



class Assignprojects(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Completed', 'Completed'),
        ('In Progress', 'In Progress')
    )
    manager = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='manager')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    pname = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(null=True,blank=True)
    deadline = models.DateField(null=True,blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return "Manager "+ self.manager.user.first_name + self.manager.user.last_name + " Assigned a Work to " + self.user.user.first_name + self.user.user.last_name