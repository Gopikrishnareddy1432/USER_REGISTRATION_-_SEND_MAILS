from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from django.core.mail import send_mail
# Create your views here.

def home(request):
    return render(request,'home.html')




def registration(request):
    uf=UserForm()
    pf=ProfileForm()
    d={'uf':uf,'pf':pf}
    if request.method=='POST' and request.FILES:
        ud=UserForm(request.POST)
        pd=ProfileForm(request.POST,request.FILES)
        if ud.is_valid() and pd.is_valid():
            USO=ud.save(commit=False)
            pw=ud.cleaned_data['password']
            USO.set_password(pw)
            USO.save()

            PFO=pd.save(commit=False)
            PFO.user=USO
            PFO.save()


            send_mail('User registration',
            'if we need any requirement pls click on below link www.mia khalifa.com',
            '183a1a0108@gmail.com',
            [USO.email],fail_silently=True)




            return HttpResponse('registration is successfully')


    return render(request,'registration.html',d)