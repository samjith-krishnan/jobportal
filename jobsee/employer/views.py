from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import *
from django.views.generic import TemplateView,CreateView,ListView,DetailView,View
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from .models import *

# Create your views here.

def signin_requered(fn):

    def wrapper(request,*args,**kw):
        if not request.user.is_authenticated:

            messages.error(request,'you must login')
            return redirect('signin')
        
        else:
            return fn(request,*args,**kw)
        
    return wrapper


class CompanyAddView(CreateView):
    template_name='company-add.html'
    form_class=CompanyAddForm
    success_url=reverse_lazy('employer')

    def form_valid(self,form):
        user=self.request.user
        if user.is_employer:
            form.instance.user=user
            try:
              super().form_valid(form)
              messages.success(self.request,'successfully added')

            except Exception as e:
                messages.error(self.request,'error at adding company')
            return redirect('employer')
        else:
            messages.error(self.request,'failed attempt')
            return redirect('employerlog')
        

@method_decorator(signin_requered,name='dispatch')       
class CompanyView(ListView):
    model = Company
    template_name = 'company-list.html'
    context_object_name = 'todos'


@method_decorator(signin_requered,name='dispatch')
class CompanyDetailView(DetailView):
    model=Company
    template_name='company-detail.html'
    context_object_name='comp'
    pk_url_kwarg='id'


@method_decorator(signin_requered,name='dispatch')
class CompanyDelete(View):
    def get(self,request,*args,**kw):

        id=kw.get('id')
        isowner=request.user.company.id
        if id==isowner:
            try:
               Company.objects.get(id=id).delete()
               messages.success(request,'company deleted')
               return redirect('index')
            
            except Exception as e:
               messages.error(request,'error occured while deleting..')
               return redirect(request,'index')
        else:
            messages.error(request,'user error')
            return redirect(request,'index')

            

class JobAddView(CreateView):
    template_name='job-add.html'
    form_class=JobAddForm
    success_url=reverse_lazy('employer')

    def form_valid(self,form):
        form.instance.user=self.request.user
        form.instance.company=self.request.user.company
        
        try:
            super().form_valid(form)
            messages.success(self.request,"job added")
            return redirect('employer')
        except Exception as e:
            messages.error(self.request,'job adding failed')
            return redirect('jobadd')

class JobListView(ListView):
    model=Jobs
    template_name='job-list.html'
    context_object_name='todo'


class ApplyJobView(CreateView):
    template_name='apply.html'
    form_class=ApplyForm
    success_url='home'
    context_object_name='id'

    def form_valid(self, form):
        id=self.kwargs.get('id')
        job=Jobs.objects.get(id=id)
        company=job.company
        user=self.request.user
        form.instance.company = company
        form.instance.applicant=user
        form.instance.job=job
        super().form_valid(form)
        return redirect('home')
    
class ApplicantListView(ListView):
     model = ApplicantDetail
     template_name = 'company_applicant.html'
     context_object_name = 'comp'
     page_kwarg='id'
     
     def get_queryset(self):
         return ApplicantDetail.objects.filter(company=self.request.user.company)
         
         
