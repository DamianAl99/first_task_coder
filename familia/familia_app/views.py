from django.shortcuts import render
from django.http import HttpResponse
from familia_app.models import familia

# Create your views here.
def create_familia(request, name, surname, age, have_a_dog):
    print(bool(have_a_dog))
    familia.objects.create(name=name, surname=surname, age=float(age), have_a_dog=have_a_dog)
    context = get_familiares(familia)
    return render(request, 'index.html', context=context)

def list_familia(request):
    context = get_familiares(familia)
    return render(request, 'index.html', context=context)

def get_familiares(familia):
    all_familia = familia.objects.all()
    return {
        'familiares':all_familia,
    }