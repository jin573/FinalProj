from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Post, Category
from django.core.exceptions import PermissionDenied
from .forms import CommentForm

def new_comment(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else:
            return redirect(post.get_absolute_url())

    else :
        raise PermissionDenied

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['item', 'hook_text', 'context', 'head_image', 'price', 'product', 'category', 'msg', 'restock']

    template_name = 'shoesmall/post_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['item', 'hook_text', 'context', 'head_image', 'price', 'product', 'category', 'msg', 'restock']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/shoes_list/')

class PostList(ListView):
    model = Post
    ordering = '-pk'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context



class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['comment_form'] = CommentForm
        return context

class PostSearch(PostList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        post_list = Post.objects.filter(
            Q(item__contains=q) | Q(hook_text__contains=q)
        ).distinct()
        return post_list

    def get_context_data(self, **kwargs):
        context = super(PostSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'검색한 단어 : {q} ({self.get_queryset().count()})'
        return context

def category_page(request, slug):
    category = Category.objects.get(slug=slug)

    return render(
        request,
        'shoesmall/post_list.html',
        {
            'post_list': Post.objects.filter(category=category),
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'category': category,
        }
    )


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