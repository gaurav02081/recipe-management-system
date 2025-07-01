from django.shortcuts import render
from .models import Recipe

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

    return render(request, 'vege/recipes.html', {
        'recipe_name': recipe_name,
        'recipe_description': recipe_description,
        'recipe_image': recipe_image,
    })


