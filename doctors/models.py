from django.db import models

# Create your models here.
class DoctorRegister(models.Model):

    name = models.CharField(max_length=30,verbose_name="Ad")
    surname = models.CharField(max_length=30,verbose_name="Soyad")
    email = models.EmailField(max_length=50,verbose_name="Email")
    password = models.CharField(max_length=40,verbose_name="Parol")
    adress = models.CharField(max_length=100,verbose_name="Unvan")
    zipp = models.CharField(max_length=30,verbose_name="ZIP")
    tel = models.CharField(max_length=35,verbose_name="Tel")
    mob  = models.CharField(max_length=50,verbose_name="Mob")
    fax = models.CharField(max_length=30,verbose_name="Fax",default="Qeyd Edilmiyib")
    wep = models.CharField(max_length=30,verbose_name="Wep")
    borndate = models.CharField(max_length=30,verbose_name="Dogum Tarixi")
    ixtisas = models.CharField(max_length=30,verbose_name="Ixtisas")
    verzife = models.CharField(max_length=30,verbose_name="Vezife")
    elmiderece = models.CharField(max_length=30,verbose_name="Elmi Derece")
    isYeri = models.CharField(max_length=30,verbose_name="Is Yeri")
    mezunOlmaTarixi = models.CharField(max_length=30,verbose_name="Mezun Oldugu Tarix")
    mezunOlduquYer = models.CharField(max_length=30,verbose_name="Mezun Olduqu Yer")
    fakulte = models.CharField(max_length=30,verbose_name="Fakulte")

    def __str__(self):
        return self.name
    
