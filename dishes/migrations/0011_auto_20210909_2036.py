# Generated by Django 3.2.5 on 2021-09-09 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0010_alter_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishingredient',
            name='dish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dishes.dish'),
        ),
        migrations.AlterField(
            model_name='dishingredient',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dishes.ingredient'),
        ),
    ]
