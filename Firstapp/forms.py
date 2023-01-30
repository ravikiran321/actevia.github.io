from django import forms
from Firstapp.models import Employee
from Firstapp.models import Recruiter
from Firstapp.models import HR
from django.contrib.admin.widgets import AdminSplitDateTime


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        '''fields = ("slno","name","yearofexp","education","keyskills","detailedskills","interviewscore","prefferedworklocation",
        "currentsalary","expectedsalary","doj")'''
        fields = "__all__"
        
class ResourceForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        fields = "__all__"

class HRForm(forms.ModelForm):
   # L1interviewdatetime = forms.SplitDateTimeField(widget=AdminSplitDateTime())
    #L2interviewdatetime = forms.SplitDateTimeField(widget=AdminSplitDateTime())
    class Meta:
        model = HR
        fields = "__all__"
    
    '''def __init__(self, *args, **kwargs):
        super(HRForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'''

class HRForm1(forms.Form):
    data_time_input = forms.DateField(widget=AdminSplitDateTime())