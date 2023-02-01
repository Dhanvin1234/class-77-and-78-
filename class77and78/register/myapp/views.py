from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def register(request,method):
    if request.method=="post":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username") 
            messages.success(request,"your account has been created")
            return redirect("login")
    else:
        form=UserCreationForm() 
    return render(request,"templates/register.html",{"form":form})
def profile(request):
    return render(request,"templates/profile.html")
    

# Create your views here.
