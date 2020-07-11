from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth import login 
from passlib.hash import sha256_crypt



# Create your views here.
def register(request):
    print(request.method,"METHODD")
    if request.method == "POST":
        form = forms.DoctorForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            surname = form.cleaned_data.get("surname")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            adress = form.cleaned_data.get("adress")
            zipp = form.cleaned_data.get("zipp")
            tel = form.cleaned_data.get("tel")
            mob = form.cleaned_data.get("mob")
            fax = form.cleaned_data.get("fax")
            wep = form.cleaned_data.get("wep")
            borndate = form.cleaned_data.get("borndate")
            ixtisas = form.cleaned_data.get("ixtisas")
            verzife = form.cleaned_data.get("verzife")
            elmiderece = form.cleaned_data.get("elmiderece")
            isYeri = form.cleaned_data.get("isYeri")
            mezunOlmaTarixi = form.cleaned_data.get("mezunOlmaTarixi")
            mezunOlduquYer = form.cleaned_data.get("mezunOlduquYer")
            fakulte = form.cleaned_data.get("fakulte")


            newDoctor = models.DoctorRegister()
            newDoctor.name = name
            newDoctor.surname = surname
            newDoctor.email = email
            newDoctor.password = sha256_crypt.encrypt(password) 
            newDoctor.adress = adress
            newDoctor.zipp = zipp
            newDoctor.tel = tel
            newDoctor.mob = mob
            newDoctor.fax = fax
            newDoctor.wep = wep
            newDoctor.borndate = borndate
            newDoctor.ixtisas = ixtisas
            newDoctor.verzife = verzife
            newDoctor.elmiderece = elmiderece
            newDoctor.isYeri = isYeri
            newDoctor.mezunOlduquYer = mezunOlduquYer
            newDoctor.mezunOlmaTarixi = mezunOlmaTarixi
            newDoctor.fakulte = fakulte
            newDoctor.save()
            #login(request,newDoctor) bu nedense isdemedi yeqinki djangonun surumundendi

            return redirect("index")
        else:
            print("POSTELSE")
            form = forms.DoctorForms()
            content={
                "form":form,
            }
            return render(request,"doctorRegister.html",content)



            

    else:
        form = forms.DoctorForms()
        content={
            "form":form,
        }
        return render(request,"doctorRegister.html",content)

