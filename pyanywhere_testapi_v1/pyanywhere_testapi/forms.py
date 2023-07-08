from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class newUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        field = ("username","email","password1","password2")
    def registrationEvent(self, commit = True):
        user = super(newUserForm,self).registrationEvent(commit=False)
        user.email = self.cleaned_data('email')
        if commit:
            user.save()
        return user
