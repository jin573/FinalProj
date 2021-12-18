from django.views.generic import ListView, DetailView
from .models import Post, Category

class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

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