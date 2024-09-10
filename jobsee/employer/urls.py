from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [

   path('company/add',CompanyAddView.as_view(),name='companyadd'),
   path('company/list',CompanyView.as_view(),name='companylist'),
   path('job/add',JobAddView.as_view(),name='jobadd'),
   path('job/list',JobListView.as_view(),name='joblist'),
   path('company/detail/<int:id>',CompanyDetailView.as_view(),name='companydetail'),
   path('company/delete/<int:id>',CompanyDelete.as_view(),name='comp-delete'),
   path('apply/<int:id>',ApplyJobView.as_view(),name='apply'),
   path('applicant/<int:id>',ApplicantListView.as_view(),name='applicant')


 

]
