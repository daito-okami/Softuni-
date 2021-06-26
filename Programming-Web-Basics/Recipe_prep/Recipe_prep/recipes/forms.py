from django import forms

from Recipe_prep.recipes.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class DeleteRecipeForm(RecipeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for(_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
