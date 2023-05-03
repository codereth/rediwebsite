from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def fashion(request):
    return render(request, 'main/fashion.html')

def gifts(request):
    return render(request, 'main/gifts.html')

def ideas(request):
    return render(request, 'main/ideas.html')

def news(request):
    return render(request, 'main/news.html')

