from django.shortcuts import render

# Create your views here.

from .models import Tanulo, Valasztas, Foglalkozas

def home_view(request, *args, **kwargs):

    tanulok= Tanulo.objects.all()
    kontextus = {
    "a": 123,
    "b": "blablabla",
    "l": [1,3,5,7,9],
    "tanulo" : tanulok,
    }

    print(f"a kontextusban az a értéke: {kontextus['a']}")
    return render(request, "home.html", kontextus) 
