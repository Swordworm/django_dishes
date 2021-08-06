from django import forms


class DishForm(forms.Form):
    def __init__(self, *args, **kwargs):
        ingredients = kwargs.pop('ingredients')
        super().__init__(*args, **kwargs)

        for index, ingredient in enumerate(ingredients, start=1):
            self.fields[ingredient['id']] = forms.IntegerField(
                label=ingredient['name'],
                initial=ingredient['quantity'],
                widget=forms.NumberInput(
                    attrs={
                        'style': 'max-width: 50px;'
                    }
                )
            )


