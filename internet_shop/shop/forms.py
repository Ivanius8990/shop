from django import forms

from shop.models import Category, Users


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['first_name','last_name','email']
        widgets={
            'first_name': forms.TextInput(attrs={'class': 'input','placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'class': 'input','placeholder': 'Фамилия'}),
            'email': forms.EmailInput(attrs={'class': 'input','placeholder': 'email'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""