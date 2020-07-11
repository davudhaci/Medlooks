from django.shortcuts import render,redirect
from . import forms,models
from passlib.hash import sha256_crypt
from django.contrib import messages

# Create your views here.


def register(request):

    if request.method == "POST":
        form = forms.EnterpriseForms(request.POST)

        if form.is_valid():
            enterprise = models.EnterpriseRegister()
            enterprise.enterpriseName = form.cleaned_data.get("enterpriseName")
            enterprise.email = form.cleaned_data.get("email")
            enterprise.password = sha256_crypt.encrypt(form.cleaned_data.get("password"))
            enterprise.address = form.cleaned_data.get("address")
            enterprise.zipp = form.cleaned_data.get("zipp")
            enterprise.tel = form.cleaned_data.get("tel")
            enterprise.mob = form.cleaned_data.get("mob")
            enterprise.fax = form.cleaned_data.get("fax")
            enterprise.wep = form.cleaned_data.get("wep")
            enterprise.rejim = form.cleaned_data.get("rejim")
            enterprise.leader = form.cleaned_data.get("leader")
            enterprise.save()
            messages.success(request,"Qeydiyatdan Kecdin :d")
            return redirect("index")

        else:
            # Xanalarda da requeremnts lerden hansisa yanlis gedtikde else daxil olur
         
            form = forms.EnterpriseForms()

            conxten={
                "form":form
            }
            return render(request,"enterpriseregister.html",conxten)




    else: 

        form = forms.EnterpriseForms()

        conxten={
            "form":form
        }
        return render(request,"enterpriseregister.html",conxten)

def login(request):
    pass


def logout(request):
    pass
