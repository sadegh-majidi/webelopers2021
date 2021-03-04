from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from store.models import ContactRequest


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


class ContactUsForm(forms.ModelForm):
    title = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    text = forms.CharField(min_length=10, max_length=250, required=True)

    class Meta:
        model = ContactRequest
        fields = ('title', 'email', 'text',)

    def save(self, commit=True):
        contact_request = ContactRequest.objects.create(
            title=self.cleaned_data['title'],
            email=self.cleaned_data['email'],
            text=self.cleaned_data['text']
        )
        send_mail(
            contact_request.title,
            f'{contact_request.text} {contact_request.email}',
            'sadeghmajidiyazdi@gmail.com',
            ['sadegh0211380@gmail.com'],
            fail_silently=False,
        )
        return contact_request



