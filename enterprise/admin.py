from django.contrib import admin
from .models import EnterpriseRegister
# Register your models here.


@admin.register(EnterpriseRegister)
class ArticleAdmin(admin.ModelAdmin):


    class Meta:
        model = EnterpriseRegister