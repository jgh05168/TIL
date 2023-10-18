from rest_framework import serializers
from .models import Article

# ModelSerializer : Django 모델과 연결된 Serializer 클래스
class ArticleListSerializer(serializers.ModelSerializer):       
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'