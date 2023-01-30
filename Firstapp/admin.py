from django.contrib import admin
from .models import Employee
from .models import Recruiter
from .models import HR
# Register your models here.

# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ("slno","name","yearofexp","education","keyskills","detailedskills","interviewscore","prefferedworklocation","currentsalary","expectedsalary","doj","status")
admin.site.register(Employee)
admin.site.register(Recruiter)
admin.site.register(HR)
