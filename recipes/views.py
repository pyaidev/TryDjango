from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Recipe, RecipeIngredient
from .forms import RecipesForm, RecipeIngredientForm
from django.forms import modelformset_factory


def recipe_list_view(request):
    recipes = Recipe.objects.all()

    context = {
        'object_list': recipes
    }

    return render(request, 'recipes/list.html', context)


def recipe_detail_view(request, slug=None):
    obj = None
    if slug is not None:
        obj = Recipe.objects.get(slug=slug)


    context = {
        'object': obj
    }

    return render(request, 'recipes/detail.html', context)


@login_required
def recipe_create_view(request):
    form = RecipesForm(request.POST or None, request.FILES or None)
    FormSet = modelformset_factory(RecipeIngredient, form=RecipeIngredientForm, extra=1)
    qs = RecipeIngredient.objects.none()
    formset = FormSet(request.POST or None, queryset=qs)
    if form.is_valid() and formset.is_valid():
        obj = form.save(commit=False)
        obj.user_id = request.user.id
        obj.save()
        form.save_m2m()

        for form in formset:
            obj2 = form.save(commit=False)
            if form.cleaned_data.get('ingredient_name') and form.cleaned_data.get('quantity'):
                obj2.recipe_id = obj.id
                obj2.save()

        return redirect('recipes:detail', obj.slug)

    context = {
        'form': form,
        'formset': formset,
    }

    return render(request, 'recipes/create.html', context)


def recipe_edit_view(request, pk=None):
    obj = None
    context = {

    }
    if pk is not None:
        obj = Recipe.objects.get(id=pk)
        form = RecipesForm(request.POST or None, request.FILES or None, instance=obj)
        FormSet = modelformset_factory(RecipeIngredient, form=RecipeIngredientForm, extra=1)
        qs = RecipeIngredient.objects.filter(recipe_id=pk)
        formset = FormSet(request.POST or None, queryset=qs)
        context['form'] = form
        context['formset'] = formset
        if form.is_valid() and formset.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form.save_m2m()

            for form in formset:
                obj2 = form.save(commit=False)
                if form.cleaned_data.get('ingredient_name') and form.cleaned_data.get('quantity'):
                    obj2.recipe_id = obj.id
                    obj2.save()

            return redirect('recipes:detail', obj.slug)

    return render(request, 'recipes/edit.html', context)


def recipe_delete_view(request, pk=None):

    obj = None
    if pk is not None:
        obj = Recipe.objects.get(id=pk)
        if request.method == 'POST':

            obj.delete()
            return redirect('recipes:list')

    context = {
        'object': obj
    }

    return render(request, 'recipes/delete.html', context)



