from django.contrib import admin
from .models import Recipe, RecipeIngredient, Tag


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientInline, )
    search_fields = ['name']
    prepopulated_fields = {"slug": ('user', 'name')}
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ('tags', )
    # fields = ('user', 'name', 'slug', 'is_active', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
                'fields': ('user', 'name', 'img', 'slug', 'tags', 'is_active')
                }
         ),
        # ('Timestamp', {
        #     'fields': ('created_at', 'updated_at')
        #      }
        #  )
    )

class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'ingredient_name', 'recipe', 'get_recipe_user', 'quantity', 'unit', 'is_active', 'created_at')
    list_filter = ('recipe', 'unit', 'created_at', 'is_active')
    search_fields = ('name', 'recipe__name')
    list_display_links = ('ingredient_name', 'id')
    list_per_page = 50
    list_editable = ('unit', )
    search_help_text = 'search with name and recipes'
    date_hierarchy = 'created_at'
    autocomplete_fields = ('recipe', )

    def get_recipe_user(self, obj):
        return obj.recipe.user


admin.site.register(Tag)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
