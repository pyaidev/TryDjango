# Generated by Django 4.1 on 2022-08-20 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipeingredient_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.IntegerField(choices=[(0, 'KG'), (1, 'L'), (2, 'SHT')], default=0),
        ),
    ]
