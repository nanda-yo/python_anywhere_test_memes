from django.shortcuts import render,redirect
from .forms import newUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.template import loader

def registrationRequest(Request):
    if Request.method == "POST":
        form = newUserForm(Request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(Request, "Registration successful")
            login(Request,user)

            return redirect("Registration")
        messages.error(Request,"Registration refused, invalid information")
    form = newUserForm()
    return render(request=Request,template_name="registration.html",context={"registration_form":form})



def index(Request):
    #template = loader.get_template('index.html')
    return render(request=Request, template_name="index.html")
