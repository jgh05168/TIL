from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form' : form
#     }
#     return render(request, 'articles/new.html', context)


def create(request):
    '''
    if 요청의 메서드가 POST라면:
        create 로직
    else:
        new 로직
    '''

    if request.method == 'POST':        # create 진행
        # form 사용 후 create 방식
        form = ArticleForm(request.POST)
        if form.is_valid():         # 유효성 검사
            article = form.save()   # save()는 반환값을 갖고 있다.
            return redirect('articles:detail', article.pk)
        # # 유효성 검사를 통과하지 못했을 경우. 
        # context = {
        #     'form': form    # 실패한 이유(Error)가 함께 전달된다.
        # }
        # return render(request, 'articles/new.html', context)

    else:       # new 진행
        form = ArticleForm()        # POST가 아닐 때는 과거 단순히 form 인스턴스 생성

    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)        # 수정하고자 하는 객체를 인스턴스 인자로 넣어주면 기존의 값을 인식할 수 있다. 
#     context = {
#         'article': article,
#         'form' : form
#     }
#     return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    # return redirect('articles:detail', article.pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)      # 기존의 값들을 인스턴스 인자로 받아와야해@!
        if form.is_valid():
            form.save()     # create에서 지정해주었으므로 다시 변수에 값을 저장할 필요가 없다.
            return redirect('articles:detail', article.pk)
        
    else:
        form = ArticleForm(instance=article)        # 수정하고자 하는 객체를 인스턴스 인자로 넣어주면 기존의 값을 인식할 수 있다. 
    context = {
        'article': article,
        'form' : form
    }
    return render(request, 'articles/update.html', context)