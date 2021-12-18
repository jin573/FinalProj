from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post

#def index(request):
#    items = Post.objects.all().order_by('-pk')

#    return render(
#        request,
#        'shoesmall/post_list.html',
#        {
#            'items':items,
#        }

#    )

#def single_item_page(request,pk):
#    item = Post.objects.get(pk=pk)

#    return render(
#        request,
#        'shoesmall/post_detail.html',
#        {
#            'item':item,
#        }
#    )