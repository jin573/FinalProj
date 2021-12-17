from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(
        request,
        'single_pages/shoesmall_home.html',
    )

def my_page(request):
    return render(
        request,
        'single_pages/my_page.html',
    )

def company_shoesmall(request):
    return render(
        request,
        'single_pages/company_shoesmall.html',
    )