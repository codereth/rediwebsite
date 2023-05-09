from django.shortcuts import render
from .models import Contact, Contactus, Subscriber
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    if request.method == "POST":
        if 'subscriber_email' in request.POST:
            email = request.POST['subscriber_email']
            Subscriber.objects.create(email=email)
        else:
            name = request.POST['name']
            email = request.POST['email']
            con = Contact.objects.create(name=name, email=email)

    return render(request, 'main/index.html')

@csrf_exempt
def about(request):
    if request.method == "POST":
        email = request.POST['subscriber_email']
        Subscriber.objects.create(email=email)
    return render(request, 'main/about.html')

@csrf_exempt
def contact(request):
    if request.method == "POST":
        if 'subscriber_email' in request.POST:
            email = request.POST['subscriber_email']
            Subscriber.objects.create(email=email)
        else:
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']
            con_us = Contactus.objects.create(name=name, email=email, message=message)

    return render(request, 'main/contact.html')

@csrf_exempt
def fashion(request):
    if request.method == "POST":    
        email = request.POST['subscriber_email']
        Subscriber.objects.create(email=email)

    return render(request, 'main/fashion.html')

@csrf_exempt
def gifts(request):
    if request.method == "POST":
        email = request.POST['subscriber_email']
        Subscriber.objects.create(email=email)

    return render(request, 'main/gifts.html')

@csrf_exempt
def ideas(request):
    if request.method == "POST":
        email = request.POST['subscriber_email']
        Subscriber.objects.create(email=email)

    return render(request, 'main/ideas.html')

@csrf_exempt
def news(request):
    if request.method == "POST":
        email = request.POST['subscriber_email']
        Subscriber.objects.create(email=email)
    
    return render(request, 'main/news.html')

