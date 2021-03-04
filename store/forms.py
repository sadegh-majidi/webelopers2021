from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


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

    def clean(self):
        try:
            User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            if not self.cleaned_data['password1'] == self.cleaned_data['password2']:
                raise ValidationError('گذرواژه و تکرار گذرواژه یکسان نیستند')
        else:
            raise ValidationError('نام کاربری شما در سیستم موجود است')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
