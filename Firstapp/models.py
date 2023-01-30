from django.db import models
from django.contrib.admin.widgets import AdminSplitDateTime

status = (
    ("Available","Available"),
    ("Engaged","Engaged"),
)

r_status = (
    ("Open", "Open"),
    ("Open", "Closed"),
)

onboarding_status = (
    ("YES", "YES"),
    ("NO", "NO"),
)

class Employee(models.Model):
    name = models.CharField(max_length= 100)
    yearofexp = models.FloatField()
    education = models.CharField(max_length = 300)
    keyskills = models.CharField(max_length= 500)
    detailedskills = models.TextField()
    interviewscore = models.CharField(max_length=4)
    prefferedworklocation = models.CharField(max_length=500)
    currentsalary = models.FloatField()
    expectedsalary = models.FloatField()
    doj = models.CharField(max_length= 300)
    status = models.CharField(max_length=20 , choices=status , default="Available")
    class Meta:
        db_table = "employee"


class Recruiter(models.Model):
    rid = models.CharField(max_length=5)
    companyname = models.CharField(max_length=30)
    jobarea = models.CharField(max_length=30)
    resourcerequired = models.FloatField()
    jd = models.TextField()
    resourceremaining = models.FloatField()
    r_status = models.CharField(max_length=20 , choices=r_status , default="open")
    class Meta:
        db_table = "resources"

    def __str__(self):
        return self.rid

class HR(models.Model):
    hrid = models.ForeignKey(Recruiter,blank=True, null=True,on_delete=models.CASCADE)
    file = models.FileField()
    L1interviewername = models.CharField(max_length=100)
    L1interviewdatetime  = models.DateTimeField(null=True)
    L2interviewername = models.CharField(max_length=100)
    L2interviewdatetime  = models.DateTimeField(null=True)
    status = models.CharField(max_length=20 , choices=r_status , default="open")
    onboarding = models.CharField(max_length=20 , choices=onboarding_status , default="YES")
    class Meta:
        db_table = "hr"

    def __str__(self):
        return f"{self.createdAt.strftime('%d-%m-%Y')}"

