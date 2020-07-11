from django.shortcuts import render,redirect
from . import forms,models
from passlib.hash import sha256_crypt

# Create your views here.
def register(request):

    if request.method == "POST":
        form = forms.UserRegister(request.POST)

        if form.is_valid():
            newUser = models.UserRegister()
            newUser.ad = form.cleaned_data.get("ad")
            newUser.soyad = form.cleaned_data.get("soyad")
            newUser.unvan = form.cleaned_data.get("unvan")
            newUser.zzip = form.cleaned_data.get("zzip")
            newUser.tel = form.cleaned_data.get("tel")
            newUser.wep = form.cleaned_data.get("wep")
            newUser.dogumTarixi = form.cleaned_data.get("dogumTarixi")
            newUser.fax = form.cleaned_data.get("fax")
            newUser.email =  sha256_crypt.encrypt(form.cleaned_data.get("email")) 
            newUser.parol = form.cleaned_data.get("parol")

            newUser.save()

            return redirect("index")
        else:
            form = forms.UserRegister()

            content = {
                "form":form

            }

            return render(request,"userRegister.html",content)
            

    else:

        form = forms.UserRegister()
        content = {
            "form":form,
        }

        return render(request,"userRegister.html",content) # ardicilliqa fikir ver --> request templete content

def login(request):
    pass

def logout(request):
    pass