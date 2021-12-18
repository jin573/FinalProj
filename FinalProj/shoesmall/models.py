from django.db import models
# Create your models here.

class Post(models.Model):
    item = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=30)
    head_image = models.ImageField(upload_to='shoesmall/images/%Y/%m/%d/', blank=True)
    price = models.CharField(max_length=20)
    #제조사
    #카테고리

    #tag
    msg = models.BooleanField(default=True)
    restock = models.DateField(null=True)

    def __str__(self):
        return f'{self.item}'

    def get_absolute_url(self):
        return f'/shoes_list/{self.pk}/'