from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'

#def index(request):
#    items = Post.objects.all().order_by('-pk')

#    return render(
#        request,
#        'shoesmall/post_list.html',
#        {
#            'items':items,
#        }

#    )

def single_item_page(request,pk):
    item = Post.objects.get(pk=pk)

    return render(
        request,
        'shoesmall/single_item_page.html',
        {
            'item':item,
        }
    )