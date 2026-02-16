from django import forms


class MedicineSearchForm(forms.Form):
    query = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search for medicine by brand name...',
            'autocomplete': 'off'
        })
    )
