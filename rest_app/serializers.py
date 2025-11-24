from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    recipe_img = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = '__all__'

    def get_recipe_img(self, obj):
        request = self.context.get('request')
        if obj.recipe_img:
            return request.build_absolute_uri(obj.recipe_img.url)
        return None
