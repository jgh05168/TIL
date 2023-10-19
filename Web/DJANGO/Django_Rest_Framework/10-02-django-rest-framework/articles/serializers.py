from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class CommentSerializer(serializers.ModelSerializer):
    # 내부에서만 사용가능한 새로운 article 클래스 지정(title 정보만 사용하고 싶으므로)
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',) 

    # class override
    article = ArticleSerializer(read_only=True)     # 읽기 전용 필드를 True로 설정(Meta의 read_only_field와 중복이 되기 때문에 여기서 설정)

    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article',)         # 읽기 전용 필드



class ArticleSerializer(serializers.ModelSerializer):
    # Nested_relationships
    # 댓글 목록
    comment_set = CommentSerializer(many=True, read_only=True)
    # 댓글 개수
    # 새로운 serializerField 사용
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta:
        model = Article
        fields = '__all__'