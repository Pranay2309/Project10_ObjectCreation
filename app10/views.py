from django.shortcuts import render
from app10.models import Person

# Create your views here.
def form(request):
    return render(request, "form.html")

def show(request):
    data = {
        'name' : request.POST.get('name'),
        'email' : request.POST.get('email')

    }
    return render(request, "show.html", data)

def create(request):
    Person.objects.create(name="xyz", email="xyz@gmail.com")
    return render(request, "create.html")