from django.db import models

# Create your models here.
class EnterpriseRegister(models.Model):
    enterpriseName = models.CharField(max_length=50,verbose_name="Sirket Adi")
    email = models.EmailField(max_length=254,verbose_name="Email")
    password = models.CharField(max_length=50,verbose_name="Parol")
    address  = models.CharField(max_length=250,verbose_name="Unvan")
    zipp = models.CharField(max_length=50,verbose_name="ZIP")
    tel = models.CharField(max_length=50,verbose_name="Telefon")
    mob  = models.CharField(max_length=50,verbose_name="Mob")
    fax  = models.CharField(max_length=50,verbose_name="Fax")
    wep  = models.CharField(max_length=50,verbose_name="Wep")
    rejim  = models.CharField(max_length=50,verbose_name="Rejim")
    leader  = models.CharField(max_length=50,verbose_name="Rehber")

    def __str__(self):
        return self.enterpriseName
    
