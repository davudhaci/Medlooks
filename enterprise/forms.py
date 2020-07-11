from django import forms


class EnterpriseForms(forms.Form):
    enterpriseName=forms.CharField(max_length=50,label="Muesise Adi")
    email = forms.EmailField(label="Email", required=True)
    password = forms.CharField(max_length=50,label="Parol",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=50,label="Tekrar Parol",widget=forms.PasswordInput)
    address = forms.CharField(max_length=250,label="Unvan") 
    zipp = forms.CharField(max_length=20,label="ZIP") 
    tel = forms.CharField(max_length=25,label="Telefon") 
    mob = forms.CharField(max_length=50,label="Mob") 
    fax = forms.CharField(max_length=50,label="Fax") 
    wep = forms.CharField(max_length=100,label="Wep") 
    rejim  = forms.ChoiceField(choices=[("7:24","7:24"),("7:12","7:12")],label="Rejim") 
    leader = forms.CharField(max_length=50,label="Rehber")

    def clean(self):
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and password==confirm:
            content ={
                "password":password,
                "enterpriseName":self.cleaned_data.get("enterpriseName"),
                "email":self.cleaned_data.get("email"),
                "address":self.cleaned_data.get("address"),
                "zipp":self.cleaned_data.get("zipp"),
                "tel":self.cleaned_data.get("tel"),
                "mob":self.cleaned_data.get("mob"),
                "fax":self.cleaned_data.get("fax"),
                "wep":self.cleaned_data.get("wep"),
                "rejim":self.cleaned_data.get("rejim"),
                "leader":self.cleaned_data.get("leader"),                
            }
            return content
        else:
            pass #burda djangonun xeta mesjiynan xeta gondermek lazimdi seyfeye -->danger



    