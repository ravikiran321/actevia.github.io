"""Actevia_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Firstapp import views
from Firstapp.views import searchEmployeeInfo
from Firstapp.views import show
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.urls import path, include
from Actevia_Project.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup", views.SignupPage,name='signup'),
    path("",views.LoginPage,name='login'),
    path("emp" , views.emp),
    path("logout",views.LogoutPage,name='logout'),
    path("edit/<int:id>" , views.edit),
    path("update/<int:id>" , views.update),
    path("delete/<int:id>" , views.delete),
    path("edit1/<int:id>" , views.edit1),
    path("update1/<int:id>" , views.update1),
    path("edit2/<int:id>" , views.edit2),
    path("update2/<int:id>" , views.update2),
    path("delete1/<int:id>" , views.delete1),
    path("delete2/<int:id>" , views.delete2),
    path("Search",views.searchEmployeeInfo, name="search"),
    path("recruiter",views.recruiter),
    path("hr",views.hr),
    path("show",views.show),
    path("show1",views.show1),
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  

