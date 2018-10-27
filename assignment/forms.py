from django import forms
from django.core.validators import MinValueValidator, MaxLengthValidator

class GenerateRandomUserForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(50),
            MaxLengthValidator(500)
        ]
    )
