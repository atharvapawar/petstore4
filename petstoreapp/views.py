from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import Pet
from .forms import PetForm

# Create your views here.
def home(request):
    return render(request, 'petstoreapp/home.html')

def pets_list(request):
    pets = Pet.objects.all()
    #return render(request, 'petstoreapp/pets_list.html', {'pets': pets})
    name_search = request.GET.get('name_search','')
    pets = Pet.objects.filter(id__icontains=name_search)
    return render(request, 'petstoreapp/pets_list.html', {'pets': pets ,'name_search' : name_search})

def pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)   
        if form.is_valid():
            form.save()
            return redirect('pets_list')
    else:
        form = PetForm()
    return render(request, 'petstoreapp/pet_create.html', {'form': form})

def search_results(request):
    search_query = request.GET.get('search','')
    pets = Pet.objects.filter(Q(name__icontains=search_query) | Q (breed__icontains=search_query))
    return render(request, 'petstoreapp/pets_list.html', {'pets': pets, 'search_query':search_query})

def my_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('pets_list')
        else:
            pass
    return render(request, 'petstoreapp/login.html')

def my_logout(request):
    logout(request)
    return redirect('login')
    