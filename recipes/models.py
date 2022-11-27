from django.db import models
from django.utils.text import slugify

from .validators import validator_of_units
from django.db.models.signals import pre_save, post_save


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(models.Model):
    tag = models.CharField(max_length=21)

    def __str__(self):
        return self.tag

class Recipe(Timestamp):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=221)
    img = models.ImageField(null=True, upload_to='recipe')
    slug = models.SlugField(blank=True, unique=True, null=True)
    tags = models.ManyToManyField(Tag)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    # recipeingrident_set
    # <model_name>_set



class RecipeIngredient(Timestamp):
    UNITS = (
        (0, 'KG'),  # get_<fielld_name>_display
        (1, 'L'),
        (2, 'SHT'),
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=221, help_text='kamroq soz bilan tarifla')
    quantity = models.FloatField()
    # unit = models.CharField(max_length=21, validators=[validator_of_units])  # kg, l, sht
    unit = models.IntegerField(choices=UNITS, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.ingredient_name



def recipe_post_save(sender, instance, created, *args, **kwargs):
    if created:
        instance.slug = slugify(f"{instance.user_id} {instance.name}")
        instance.save()



post_save.connect(recipe_post_save, sender=Recipe)
