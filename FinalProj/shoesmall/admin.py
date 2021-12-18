from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Category, Product

# Register your models here.
admin.site.register(Post, MarkdownxModelAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Product, ProductAdmin)