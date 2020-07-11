from django.contrib import admin
from .models import DoctorRegister
# Register your models here.


@admin.register(DoctorRegister)
class ArticleAdmin(admin.ModelAdmin):


    class Meta:
        model = DoctorRegister