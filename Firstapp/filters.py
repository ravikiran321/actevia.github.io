import django_filters
from .models import Employee

class FilterEmployeeInfo(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = ["name","yearofexp","education","keyskills","detailedskills","interviewscore","prefferedworklocation","currentsalary","expectedsalary","doj","status"]
        