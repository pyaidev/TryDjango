# Generated by Django 4.1 on 2022-08-20 14:36

from django.db import migrations, models
import recipes.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipeingredient_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.CharField(max_length=21, validators=[recipes.validators.validator_of_units]),
        ),
    ]