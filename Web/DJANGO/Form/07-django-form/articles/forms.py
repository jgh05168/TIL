from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     # 사용자로부터 입력받는 내용
#     title = forms.CharField(max_length=10)  
#     content = forms.CharField(widget=forms.Textarea)      # form에는 text field가 없다. / max_length는 필수 인자가 아니다.
#     # 여러 위젯들을 사용할 수 있다.(Django 공식문서 참고)

class ArticleForm(forms.ModelForm):
    # ModelForm을 사용하더라도 위젯을 사용할 수 있다.
    # 단지 위에처럼 각각에 대한 정보를 가져와야 한다.\
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs = {
                'class': 'my_title',
                'placeholder': 'Enter the title',
                'rows': 5,
                'cols': 50
            }
        )
    )

    # 모델을 등록만 하면 된다.
    class Meta:     # 단순 Django 문법 - ArticleForm에 데한 데이터
        model = Article
        fields = '__all__'       # 전체 필드를 선택하는 명령어
        # fields = ('title', )        # 특정 필드를 지정하는 법
        # exclude = ('title', )       # 특정 필드를 제거하는 법