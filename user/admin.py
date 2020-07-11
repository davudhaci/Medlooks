from django.contrib import admin
from .models import UserRegister
# Register your models here.


@admin.register(UserRegister)
class ArticleAdmin(admin.ModelAdmin):


    class Meta:
        model = UserRegister