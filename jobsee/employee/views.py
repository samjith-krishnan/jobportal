from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,DetailView,View
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout


# Create your views here.


class IndexView(ListView):
    template_name='index.html'
    context_object_name='item'

    def get_queryset(self):
       
        return None
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['company']=Company.objects.all()
        context['job']=Jobs.objects.all()
        return context
    
class HomeView(ListView):
    template_name='home.html'
    context_object_name='item'

    def get_queryset(self):
       
        return None
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['company']=Company.objects.all()
        context['job']=Jobs.objects.all()
        return context

class EmployeeAddview(CreateView):
    template_name='employe-add.html'
    form_class=EmployeeReg
    success_url=reverse_lazy('login')

class EmployerAddview(CreateView):
    template_name='employer-add.html'
    form_class=EmployerReg
    success_url=reverse_lazy('login')

class LoginView(View):
     
     def get(self,request,*args,**kw):
        form = LoginForm

        return render(request,"login.html",{"form":form})
    
     def post(self,request,*args,**kw):

        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user:
                if user.is_employee:
                    login(request,user)
                    return redirect('home')
                elif user.is_employer:
                    login(request,user)
                    return redirect('employer')
                else:
                    return redirect('login')
            else:
                return redirect('index')
        else:
            return redirect('index')
        
def Logout(request,*args,**kw):
    logout(request)
    return redirect('index')


class CompanyJobView(ListView):
    model=Jobs
    template_name='employer.html'
    context_object_name='comp'


class Employerview(ListView):
    model=Jobs
    template_name='employerlog.html'
    context_object_name='comp'

    def get_queryset(self):
        return Jobs.objects.filter(company=self.request.user.company)
