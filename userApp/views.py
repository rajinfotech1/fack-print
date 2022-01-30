from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import NewUserForm



def register_request(request):

    if request.method == "POST":

        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("index")
        else:
            return render (request=request, template_name="user/register.html", context={"form":form})

    form = NewUserForm()
    return render (request=request, template_name="user/register.html", context={"form":form})


def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, request.POST)
        username = request.POST['username']
        password = request.POST['password']
        # if form.is_valid():
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            print("Loged in")
            return redirect("index")

        else:        
            return render(request=request, template_name="user/login.html", context={"form":form})
            
    form = AuthenticationForm()
    return render(request=request, template_name="user/login.html", context={"form":form})


@login_required
def logout_request(request):
	logout(request)
	return redirect("userApp:login")