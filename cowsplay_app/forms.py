from django import forms
from cowsplay_app.models import Cow_Model

class Cow_Form(forms.Form):
    text = forms.CharField(max_length=100)