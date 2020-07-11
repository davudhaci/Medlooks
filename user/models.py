from django.db import models

# Create your models here.
class UserRegister(models.Model):
    ad = models.CharField(max_length=50,verbose_name="Ad")
    soyad = models.CharField(max_length=50,verbose_name="Soyad")
    unvan = models.CharField(max_length=150,verbose_name="Unvan")
    zzip = models.CharField(max_length=10,verbose_name="ZIP")
    tel = models.CharField(max_length=15,verbose_name="TEL")
    fax = models.CharField(max_length=40,verbose_name="Fax")
    email = models.EmailField(verbose_name="Email")
    parol = models.CharField(max_length=40,verbose_name="Password")
    wep = models.CharField(max_length=40,verbose_name="wep")
    dogumTarixi = models.CharField(max_length=40,verbose_name="bornDate")
    def __str__(self):
        return self.ad
    