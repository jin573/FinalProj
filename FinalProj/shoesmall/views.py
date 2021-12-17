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

def single_item_page(request,pk):
    item = Post.objects.get(pk=pk)

    return render(
        request,
        'shoesmall/single_item_page.html',
        {
            'item':item,
        }
    )