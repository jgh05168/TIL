from django.contrib import admin
from . import models
# from .models import Article   # 위와 같은 기능

# Register your models here.

# Article 모델 클래스를 admin site에 등록
# admin site에 등록(register)한다.
admin.site.register(models.Article)