from django.shortcuts import render, HttpResponse
from Home.models import Contact

# Create your views here.

def home(request):
    # return HttpResponse("This is Home Page")
    return render(request, 'index.html')

def portfolio(request):
    # return HttpResponse("This is portfolio Page")
    return render(request, 'portfolio.html')

def about(request):
    # return HttpResponse("This is about Page")
    return render(request, 'about.html')


def contact(request):
    # return HttpResponse("This is Contact Page")
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        # print(name, email)
        contact = Contact(fullName=name, email=email, Phone=phone, addr= address)
        contact.save()
    return render(request, 'contact.html')


