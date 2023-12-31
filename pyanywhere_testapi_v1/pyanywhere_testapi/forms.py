from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.contrib.auth.forms import AuthenticationForm
class newUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    def registrationEvent(self, commit = True):
        user = super(newUserForm,self).registrationEvent(commit=False)
        user.email = self.cleaned_data('email')
        if commit:
            user.save()
        return user
