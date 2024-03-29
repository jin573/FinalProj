from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=30, unique=True)

    slug = slug = models.SlugField(max_length=200, unique=True, allow_unicode=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/shoes_list/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories'

class Post(models.Model):
    item = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=30)
    context = MarkdownxField()
    head_image = models.ImageField(upload_to='shoesmall/images/%Y/%m/%d/', blank=True)
    price = models.CharField(max_length=20)
    #제조사
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    #카테고리
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    #tag
    msg = models.BooleanField(default=True)
    restock = models.DateField(null=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return f'{self.item}::{self.product}'

    def get_absolute_url(self):
        return f'/shoes_list/{self.pk}/'

    def get_context_markdown(self):
        return markdown(self.context)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists() :
            return self.author.socialaccount_set.first().get_avatar_url()
        else :
            return f'https://doitdjango.com/avatar/id/487/06e7f8791372bf27/svg/{self.author.email}'
