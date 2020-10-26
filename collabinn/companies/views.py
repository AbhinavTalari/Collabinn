from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import RegistrationForm,AccountAuthenticationForm



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
            return redirect('index_view')
        else:
            context['form'] = form
            return render(request,'companies/register.html',context)
    else:
        form = RegistrationForm()
        context['form'] = form
        return render(request, 'companies/register.html', context)