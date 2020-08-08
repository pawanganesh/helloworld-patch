from django import forms
from .models import FormsModel
class MyForm(forms.Form):
    name = forms.CharField(max_length=100)

    def clean_name(self):
        print('I am from form',self.cleaned_data)
        name = self.cleaned_data['name']
        return name.upper()

class FormsModelForm(forms.ModelForm):
    class Meta:
        model = FormsModel
        fields = ['name', 'email']