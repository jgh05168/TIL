from django.db import models

# Create your models here.
class Article(models.Model):       # 클래스 상속
    # 각각이 클래스
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)       # 날짜와 시간이 모두 표현되는 datafield
    updated_at = models.DateTimeField(auto_now=True)