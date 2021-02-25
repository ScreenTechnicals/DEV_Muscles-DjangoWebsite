from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
# Create your views here.


def registerHandelling(request):
    # return HttpResponse("Registration")

    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        username = request.POST['username']
        email = request.POST['r_email']
        password = request.POST['password']
        confirmpass = request.POST['confirmpass']
        r_phone = request.POST['r_phone']
        address = request.POST['address']

        # checks
        #

        # Create user
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = f_name
        myuser.last_name = l_name
        myuser.save()
        return redirect("/")

    else:
        return HttpResponse("404")


def register(request):
    return render(request, 'registerLogin/register.html')


def login(request):
    # return HttpResponse("Login")
    if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']
         user = auth.authenticate(username = username, password = password)
         if user is not None:
             auth.login(request, user)
             return redirect("/")
         else:
             return redirect(request, "registerLogin/login.html")
    else:
        return render(request, "registerLogin/login.html")


def logout(request):
    auth.logout(request)
    return redirect("/")