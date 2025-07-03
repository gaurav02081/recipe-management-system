from django.shortcuts import render, redirect
from .models import Recipe
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def recipes(request):
    query = request.GET.get('q')
    if query:
        queryset = Recipe.objects.filter(name__icontains=query)
    else:
        queryset = Recipe.objects.all()
    recipe_name = None
    recipe_description = None
    recipe_image = None

    if request.method == 'POST':
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')
        print(recipe_name)
        print(recipe_description)
        print(recipe_image)

        Recipe.objects.create(
            name=recipe_name,
            description=recipe_description,
            image=recipe_image
        )
        # Refresh queryset after adding new recipe
        if query:
            queryset = Recipe.objects.filter(name__icontains=query)
        else:
            queryset = Recipe.objects.all()
    return render(request, 'vege/recipes.html', {
        'queryset': queryset,
        'recipe_name': recipe_name,
        'recipe_description': recipe_description,
        'recipe_image': recipe_image,
    })

def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/')


def update_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    if request.method == 'POST':
        recipe.name = request.POST.get('recipe_name')
        recipe.description = request.POST.get('recipe_description')
        if request.FILES.get('recipe_image'):
            recipe.image = request.FILES.get('recipe_image')
        recipe.save()
        return redirect('/recipes/')
    return render(request, 'vege/update_recipe.html', {
        'recipe': recipe,
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/recipes/')
        messages.error(request, 'Invalid username or password')
        return render(request, 'vege/login.html')
    return render(request, 'vege/login.html')

def registration_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password != password2:
            messages.error(request, 'Passwords do not match')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('/login/')
    return render(request, 'vege/registration.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')

