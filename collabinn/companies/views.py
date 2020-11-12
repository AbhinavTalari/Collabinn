from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import RegistrationForm,AccountAuthenticationForm,ProfileUpdateForm
from .models import Company
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required


def renderhome(request):
    return render(request,'companies/home.html')

def register_view(request):
    context={}
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
    
    
    