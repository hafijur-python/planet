from django.contrib import admin

#Register your models here.
from appli.models import Planets

# class Login(forms.FormAdmin):
# 	field=['name','password']
#  	class Meta:
#  	  model= Login
admin.site.register(Planets
)