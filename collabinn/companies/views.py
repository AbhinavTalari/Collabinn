from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import RegistrationForm,AccountAuthenticationForm,ProfileUpdateForm
from .models import Company,CollabRequest
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
import datetime


def renderhome(request):
    return render(request,'companies/home.html')

def register_view(request):
    context={}
    if request.user.is_authenticated:
        return redirect('companylist')
    if request.POST:
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            print(request.FILES)
            # uploaded_file=request.FILES['company-logo']
            # fs=FileSystemStorage()
            # fs.save(uploaded_file.name,uploaded_file)
            
            return redirect('companylist')
        else:
            context['form'] = form
            return render(request,'companies/register.html',context)
    else:
        form = RegistrationForm()
        context['form'] = form
        return render(request, 'companies/register.html', context)
    

        



    
@login_required
def list_companies_view(request):
    context={}
    companies=Company.objects.filter(is_superuser=False)
    context['companies']=companies
    
    return render(request,'companies/companylist.html',context)
    
    
@login_required
def render_profile(request):
    if request.method=='POST':
        p_form=ProfileUpdateForm(request.POST,instance=request.user)
        if p_form.is_valid():
            p_form.save()
            return redirect('companylist')

    else:
        p_form=ProfileUpdateForm(instance=request.user)
    context={'p_form':p_form}
    return render(request,'companies/profile.html',context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
    
@login_required
def invites_view(request):
    context={}
    invites=CollabRequest.objects.filter(to_user=request.user,status=1)
    context['invites']=invites
    return render(request,'companies/invites.html',context)

@login_required   
def invite_accept(request,id):
    c1= CollabRequest.objects.get(to_user=request.user,id=id)
    c1.status=3
    c1.save()
    return redirect('invites')

def outgoing_invites_view(request):
    context={}
    o_invites=CollabRequest.objects.filter(from_user=request.user,status=1)
    
    context['oinvites']=o_invites
    return render(request,'companies/outgoing.html',context)

def invite_request(request,id):
    user=Company.objects.get(company_name=request.user.company_name)
    to_user=Company.objects.get(id=id)
    location=user.location
    date=datetime.date.today()
    status=1
    user.add_relationship(to_user,status,date,location)
    user.save()
    return redirect('companylist')