from django.shortcuts import render, redirect
from .models import Recipe
from rest_framework import generics
from .serializers import RecipeSerializer
from rest_framework.permissions import AllowAny
from .forms import RecipeForm
import requests
from django.contrib import messages
from django.core.paginator import Paginator


# ---------------------------------------------------
# DRF VIEWS
# ---------------------------------------------------

class RecipeCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [AllowAny]

    def get_serializer_context(self):
        return {'request': self.request}


class RecipeDetails(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class RecipeUpdate(generics.RetrieveUpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class RecipeDelete(generics.RetrieveDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class RecipeSearchViews(generics.ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        name = self.kwargs.get('name')
        return Recipe.objects.filter(name__icontains=name)

    def get_serializer_context(self):
        return {'request': self.request}


# ---------------------------------------------------
# DJANGO TEMPLATE VIEWS
# ---------------------------------------------------

def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Recipe created successfully!")
            return redirect('index')
        else:
            messages.error(request, "Invalid form data!")
    else:
        form = RecipeForm()

    return render(request, 'create_recipe.html', {'form': form})


def update_detail(request, id):
    """Display recipe for editing"""
    try:
        recipe = Recipe.objects.get(id=id)
        form = RecipeForm(instance=recipe)
        return render(request, "recipe_update.html", {"form": form, "recipe": recipe, "recipe_id": id})
    except Recipe.DoesNotExist:
        messages.error(request, "Recipe not found!")
        return redirect('index')


def update_recipe(request, id):
    """Handle recipe update submission"""
    try:
        recipe = Recipe.objects.get(id=id)
        
        if request.method == 'POST':
            form = RecipeForm(request.POST, request.FILES, instance=recipe)
            
            if form.is_valid():
                form.save()
                messages.success(request, "Recipe Updated Successfully!")
                return redirect('index')
            else:
                messages.error(request, "Invalid form data!")
        else:
            form = RecipeForm(instance=recipe)
        
        return render(request, "recipe_update.html", {"form": form, "recipe": recipe, "recipe_id": id})
    
    except Recipe.DoesNotExist:
        messages.error(request, "Recipe not found!")
        return redirect('index')


def index(request):
    """Main page with search and pagination"""
    
    # Handle Search
    if request.method == 'POST':
        search = request.POST.get('search', '').strip()
        if search:
            results = Recipe.objects.filter(name__icontains=search)
            return render(request, 'index.html', {'data': results, 'search_query': search})
    
    # Handle Pagination
    recipes = Recipe.objects.all().order_by('-id')
    paginator = Paginator(recipes, 6)
    page = request.GET.get('page', 1)
    
    try:
        recipe_page = paginator.page(page)
    except:
        recipe_page = paginator.page(paginator.num_pages)
    
    return render(request, "index.html", {"recipe": recipe_page})


def recipe_fetch(request, id):
    """Display detailed recipe view"""
    try:
        recipe = Recipe.objects.get(id=id)
        ingredients = recipe.description.split('.') if recipe.description else []
        ingredients = [ing.strip() for ing in ingredients if ing.strip()]
        
        return render(request, "recipe_fetch.html", {
            "recipe": recipe, 
            "ingredients": ingredients
        })
    except Recipe.DoesNotExist:
        messages.error(request, "Recipe not found!")
        return redirect('index')


def recipe_delete(request, id):
    """Delete a recipe"""
    try:
        recipe = Recipe.objects.get(id=id)
        recipe.delete()
        messages.success(request, "Recipe deleted successfully!")
    except Recipe.DoesNotExist:
        messages.error(request, "Recipe not found!")
    
    return redirect('index')