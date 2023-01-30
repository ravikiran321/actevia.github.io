from django.shortcuts import render, redirect,HttpResponse
from Firstapp.forms import EmployeeForm
from Firstapp.forms import ResourceForm
from Firstapp.forms import HRForm
from Firstapp.models import Employee
from Firstapp.models import Recruiter
from Firstapp.models import HR
from Firstapp.templates.functions import handle_upload_file
from .filters import FilterEmployeeInfo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/Search")
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, "index.html", {'form':form})


def show(request):
    employees = Recruiter.objects.all()
    return render(request, "show.html", {'employees': employees})

def show1(request):
    employees = HR.objects.all()
    return render(request, "show1.html", {'employees': employees})

def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, "edit.html", {'employee': employee})

def edit1(request, id):
    employee = Recruiter.objects.get(id=id)
    return render(request, "edit1.html", {'employee': employee})

def edit2(request, id):
    employee = HR.objects.get(id=id)
    return render(request, "edit2.html", {'employee': employee})

def update(request, id):
    employee = Employee.objects.get(id = id)
    form = EmployeeForm(request.POST, instance= employee)
    if form.is_valid():
        form.save()
        return redirect('/Search')
    return render(request, "edit.html", {'employee':employee})

def update1(request, id):
    employee = Recruiter.objects.get(id = id)
    form = ResourceForm(request.POST, instance= employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, "edit1.html", {'employee':employee})

def update2(request, id):
    employee = HR.objects.get(id = id)
    form = HRForm(request.POST, instance= employee)
    if form.is_valid():
        form.save()
        return redirect('/show1')
    return render(request, "edit2.html", {'employee':employee})

def delete(request, id):
    employee = Employee.objects.get(id = id)
    employee.delete()
    return redirect("/Search")

def delete1(request, id):
    employees = Recruiter.objects.get(id = id)
    employees.delete()
    return redirect("/show")

def delete2(request, id):
    employees = HR.objects.get(id = id)
    employees.delete()
    return redirect("/show1")

def searchEmployeeInfo(request):
    employee = Employee.objects.all()
    filters = FilterEmployeeInfo(request.GET, queryset=employee)  
    context = {'filters': filters}
    return render(request,"search.html" , context)

'''def search1EmployeeInfo(request):
    employee = Recruiter.objects.all()
    filters = FilterEmployeeInfo(request.GET, queryset=employee)  
    context = {'filters': filters}
    return render(request,"search1.html" , context)'''

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    
    return render (request,'signup.html')
    

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/Search')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def recruiter(request):
    if request.method == "POST":
        form1 = ResourceForm(request.POST)
        if form1.is_valid():
            try:
                form1.save()
                return redirect("/show")
            except:
                pass
    else:
        form1 = ResourceForm()
    return render(request, "index1.html", {'form1':form1})

def hr(request):
    if request.method == "POST":
        form1 = HRForm(request.POST, request.FILES)
        if form1.is_valid():
            try:
                handle_upload_file(request.FILES['file'])
                model_instance = form1.save(commit=False)
                model_instance.save()
                form1.save()
                return redirect("/show1")
            except:
                pass
    else:
        form1 = HRForm()
    return render(request, "index2.html", {'form1':form1})

    
            