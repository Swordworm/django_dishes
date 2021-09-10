# Generated by Django 3.2.5 on 2021-09-10 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0011_auto_20210909_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishingredient',
            name='dish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dish_ingredients', to='dishes.dish'),
        ),
        migrations.AlterField(
            model_name='dishingredient',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dish_ingredients', to='dishes.ingredient'),
        ),
    ]