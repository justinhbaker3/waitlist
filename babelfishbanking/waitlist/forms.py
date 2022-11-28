from django import forms
from .models import Waiter

class SignupForm(forms.Form):
    username = forms.CharField(max_length=200, required=True)
    referrer = forms.CharField(max_length=200, required=False)

    def clean(self):
        username = self.cleaned_data.get('username')
        referrer = self.cleaned_data.get('referrer')
        if Waiter.objects.filter(username=username).exists():
            raise forms.ValidationError('username already exists')
        if referrer != '' and not Waiter.objects.filter(username=referrer).exists():
            raise forms.ValidationError('referrer does not exist')
