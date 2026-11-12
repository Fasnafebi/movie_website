from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")

        return email
class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
        }