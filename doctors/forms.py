from django import forms

class DateInput(forms.DateInput):
    input_type='date'

class DoctorForms(forms.Form):
    name = forms.CharField(max_length=50,label="Ad")
    surname = forms.CharField(max_length=50,label="Soyad")
    email = forms.EmailField(max_length=50,label="Email")
    password = forms.CharField(max_length=50,label="Parol",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=50,label="Tekrar Parol",widget=forms.PasswordInput)
    adress = forms.CharField(max_length=250,label="Unvan")
    zipp = forms.CharField(max_length=20,label="ZIP")
    tel = forms.CharField(max_length=25,label="Telefon Nomresi")
    mob = forms.CharField(max_length=30,label="Mob")
    fax = forms.CharField(max_length=30,label="Fax",required=False) 
    wep = forms.CharField(max_length=30,label="Wep")
    borndate = forms.DateField(widget=DateInput,label="Dogum Tarixi")
    ixtisas = forms.CharField(max_length=50,label="Ixtisas")
    verzife = forms.CharField(max_length=50,label="Vezife")
    elmiderece = forms.CharField(max_length=30,label="Elmi Derece")
    isYeri = forms.CharField(max_length=150,label="Is Yeri")
    mezunOlmaTarixi = forms.DateField(widget=DateInput,label="Mezun Olma Tarixi")
    mezunOlduquYer = forms.CharField(max_length=100,label="Mezun Olduqu Yer")
    fakulte = forms.CharField(max_length=100,label="Fakulte")

    def clean(self):
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and password==confirm:
            content={
                "password":password,
                "name":self.cleaned_data.get("name"),
                "surname":self.cleaned_data.get("surname"),
                "email":self.cleaned_data.get("email"),
                "adress":self.cleaned_data.get("adress"),
                "zipp":self.cleaned_data.get("zipp"),
                "tel":self.cleaned_data.get("tel"),
                "mob":self.cleaned_data.get("mob"),
                "fax":self.cleaned_data.get("fax"),
                "wep":self.cleaned_data.get("wep"),
                "borndate":self.cleaned_data.get("borndate"),
                "ixtisas":self.cleaned_data.get("ixtisas"),
                "elmiderece":self.cleaned_data.get("elmiderece"),
                "isYeri":self.cleaned_data.get("isYeri"),
                "mezunOlmaTarixi":self.cleaned_data.get("mezunOlmaTarixi"),
                "mezunOlduquYer":self.cleaned_data.get("mezunOlduquYer"),
                "fakulte":self.cleaned_data.get("fakulte"),
                "verzife":self.cleaned_data.get("verzife")
            }
            return content
        else:
            pass #django nun xeta mesinjindan isdfade eliyib seyfeye xeta mesaji at -->danger