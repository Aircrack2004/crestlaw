from django import forms

class RepresentativeForm(forms.Form):
    name = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=15)
    occupation = forms.CharField(max_length=100)
    marital_status = forms.CharField(max_length=100)
    monthly_income = forms.DecimalField(max_digits=10, decimal_places=2)
    email = forms.EmailField()
    id_card_front = forms.ImageField()
    id_card_back = forms.ImageField()
