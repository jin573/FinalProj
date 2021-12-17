from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=30) #상품명
    hook_text = models.CharField(max_length=30) #간단한 소개

    price = models.CharField(max_length=30) #상품 가격

    # product는 제조사 모델이 작성된 후 작성하기
    # category는 카테고리 모델이 작성된 후 작성하기

    # tag는 태그 모델이 작성된 후 작성하기
    # size는 나중에..

    def __str__(self):
        return f'{self.name}'
