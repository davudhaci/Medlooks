from django import forms

class DateInput(forms.DateInput):
    input_type='date'

class UserRegister(forms.Form):
    ad = forms.CharField(max_length=50,label="Ad")
    soyad = forms.CharField(max_length=50,label="Soyad")
    unvan = forms.CharField(max_length=250,label="Unvan")
    zzip = forms.CharField(max_length=50,label="ZIP")
    tel = forms.CharField(max_length=50,label="Telefon")
    wep = forms.CharField(max_length=50,label="Wep")
    dogumTarixi = forms.DateField(widget=DateInput,label="Dogum Tarixi")
    fax = forms.CharField(max_length=50,label="Fax")
    email  = forms.EmailField(max_length=250,label="Email")
    parol = forms.CharField(max_length=50,label="Parol",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=50,label="Tekrar Parol",widget=forms.PasswordInput)



    def clean(self):
        ad = self.cleaned_data.get("ad")
        soyad = self.cleaned_data.get("soyad")
        unvan = self.cleaned_data.get("unvan")
        zzip = self.cleaned_data.get("zzip")
        tel = self.cleaned_data.get("tel")
        wep = self.cleaned_data.get("wep")
        dogumTarixi = self.cleaned_data.get("dogumTarixi")
        fax = self.cleaned_data.get("fax")
        email = self.cleaned_data.get("email")
        confirm = self.cleaned_data.get("confirm")
        parol = self.cleaned_data.get("parol")

        if parol and parol==confirm:
            contex={
                "ad":ad,
                "soyad":soyad,
                "unvan":unvan,
                "zzip":zzip,
                "tel":tel,
                "wep":wep,
                "dogumTarixi":dogumTarixi,
                "fax":fax,
                "email":email,
                "parol":parol,


            }
            return contex
        else:
            pass # burda django mesaji isifade eliyerek ekrana xeta mesji gonder


