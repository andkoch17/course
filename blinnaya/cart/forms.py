from django import forms

PRODUCT_AMOUNT_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddPancakeForm(forms.Form):
    amount = forms.TypedChoiceField(label='Кол-во' ,choices=PRODUCT_AMOUNT_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

