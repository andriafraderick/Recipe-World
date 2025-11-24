from django.urls import path
from . import views

urlpatterns = [

    # DRF API ENDPOINTS
    path('api/recipes/', views.RecipeCreateView.as_view(), name='api-recipes'),
    path('detail/<int:pk>/', views.RecipeDetails.as_view(), name="detail"),
    path('update/<int:pk>/', views.RecipeUpdate.as_view(), name="update-recipe"),
    path('delete/<int:pk>/', views.RecipeDelete.as_view(), name='delete-recipe'),
    path('search/<path:name>/', views.RecipeSearchViews.as_view(), name='search'),

    # TEMPLATE VIEWS
    path('', views.index, name='index'),
    path('create/', views.create_recipe, name='create_recipe'),
    path('update_detail/<int:id>/', views.update_detail, name='update_detail'),
    path('update_recipe/<int:id>/', views.update_recipe, name='update_recipe'),
    path('recipe_fetch/<int:id>/', views.recipe_fetch, name='recipe_fetch'),
    path('recipe_delete/<int:id>/', views.recipe_delete, name='recipe_delete'),
]
