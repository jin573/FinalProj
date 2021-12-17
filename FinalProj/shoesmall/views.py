from django.shortcuts import render
from .models import Post

def index(request):
    items = Post.objects.all().order_by('-pk')

    return render(
        request,
        'shoesmall/index.html',
        {
            'items':items,
        }

    )