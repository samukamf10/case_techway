from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request,"page_app/partial/home.html")

def contato (request):
    return render(request, "page_app/partial/contato.html")

def welcome (request):
    return render(request, "page_app/partial/welcome.html")

def footer (request):
    return render(request, "page_app/partial/footer.html")

def header (request):
    return render(request, "page_app/partial/header.html")

def services (request):
    return render(request, "page_app/partial/services.html")

def index (request):
    return render(request,"page_app/global/index.html")