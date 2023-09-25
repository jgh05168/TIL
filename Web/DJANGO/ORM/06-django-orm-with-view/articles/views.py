from django.shortcuts import render, redirect       # redirect : 재요청
from .models import Article

# Create your views here.
def index(request):
    # 모델.objects.all()
    articles = Article.objects.all()       # 하나의 조회를 위한 코드   -> 반환값 : QuerySet
    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)


def detail(request, pk):        # variable routing의 변수 이름과 매칭이 되야한다.
    article = Article.objects.get(pk=pk)  # 왼쪽 pk : 검색값, 오른쪽 pk: variable routing에서 온 변수 이름
    # Article.objects.get(id=pk)    # 이것과 위와 같은 뜻이다.
    context = {
        'article': article
    }

    return render(request, 'articles/detail.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    # # 인스턴스를 만들어서 하나하나 데이터를 넣는 방법
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 초기값으로 인스턴스를 만드는 방법
    article = Article(title = title, content = content)     # 저장되기 전에 유효성검사를 실행
    article.save()

    # # 쿼리셋의 Create method를 사용하는 방법
    # Article.objects.create(title = title, content = content)

    # return render(request, 'articles/create.html')
    # rendering을 하는 것이 아닌 redirect를 한다.
    return redirect('articles:index')


def delete(request, pk):        # variable routing
    # 1. 몇 번 게시글을 삭제할 것인지 조회
    article = Article.objects.get(pk=pk)
    # 2. 조회한 게시글을 삭제
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 수정하고자 하는 게시글을 조회
    article = Article.objects.get(pk=pk)
    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', article.pk)
