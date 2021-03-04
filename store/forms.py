from django import forms
from django.contrib.auth.models import User


class CustomSignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=70)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)
    password1 = forms.CharField(max_length=50)
    password2 = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
