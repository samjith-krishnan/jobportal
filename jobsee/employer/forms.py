from employee.models import Company,Jobs,ApplicantDetail
from django import forms



class CompanyAddForm(forms.ModelForm):
    class Meta:
        model=Company
        fields=['company_name','location','description']

class JobAddForm(forms.ModelForm):
    class Meta:
        model=Jobs
        fields=['job_title','description','salary']

class ApplyForm(forms.ModelForm):
    class Meta:
        model=ApplicantDetail
        fields=['coverletter']
        