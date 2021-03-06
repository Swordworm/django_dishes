# Generated by Django 3.2.5 on 2021-08-08 15:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0005_auto_20210808_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)])),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dishes.ingredient')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='dish',
        ),
        migrations.AddField(
            model_name='order',
            name='dish',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dishes.dish'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='OrderDish',
        ),
        migrations.AddField(
            model_name='orderingredient',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_dish', to='dishes.order'),
        ),
        migrations.AddField(
            model_name='order',
            name='ingredients',
            field=models.ManyToManyField(through='dishes.OrderIngredient', to='dishes.Ingredient'),
        ),
    ]
