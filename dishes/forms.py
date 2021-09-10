from django import forms

from dishes.models import Order, OrderIngredient, Ingredient


class OrderForm(forms.ModelForm):
    ingredient = forms.ModelChoiceField(
        label='',
        queryset=Ingredient.objects.all(),
        to_field_name='name',
        widget=forms.TextInput(
            attrs={
                'style': 'width: 70%',
                'readonly': 'readonly'
            }
        ),
    )
    quantity = forms.IntegerField(
        label='',
        widget=forms.NumberInput(
            attrs={'style': 'width: 30%'}
        )
    )

    class Meta:
        model = OrderIngredient
        fields = ('ingredient', 'quantity')


def get_order_formset(*, extra):
    return forms.modelformset_factory(
        OrderIngredient,
        OrderForm,
        extra=extra,
    )





