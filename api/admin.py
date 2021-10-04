from django.contrib import admin
from .models import Catagory,Subcatagory,Ad

model_list=[Catagory,Subcatagory,Ad]
for model in model_list:
    admin.site.register(model)
# Register your models here.
