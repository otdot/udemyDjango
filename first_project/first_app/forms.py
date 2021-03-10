from django import forms
from first_app.models import User

class MyNewForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['f_name', 'l_name', 'e_mail']
