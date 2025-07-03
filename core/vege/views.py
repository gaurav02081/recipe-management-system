from django.shortcuts import render, redirect
from .models import Recipe
from django.http import HttpResponse

# Create your views here.
def recipes(request):
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