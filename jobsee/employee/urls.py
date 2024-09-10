from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('emp/add',EmployeeAddview.as_view(),name='emp-add'),
    path('empr/add',EmployerAddview.as_view(),name='empr-add'),
    path('login',LoginView.as_view(),name='login'),
    path('home',HomeView.as_view(),name='home'),
    path('user/login',Logout,name='logout'),
    path('company/job',CompanyJobView.as_view(),name='employerlog'),
    path('company/job',Employerview.as_view(),name='employer')

    



]
