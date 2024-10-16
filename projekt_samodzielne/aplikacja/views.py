from django.shortcuts import render
from .models import model_1

# Create your views here.
def views_main(request):
    dane_z_modelu = model_1.objects.all()
    return(render(request,'index.html',context={"dane_z_modelu": dane_z_modelu}))