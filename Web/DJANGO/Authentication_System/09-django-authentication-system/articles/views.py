from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

from django.contrib.auth.decorators import login_required       # 회원 인증


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


@login_required         # 로그인 한 사람만 create를 실행할 수 있도록 데코레이터 설정(lock을 걸어주는 역할)
# 로그인을 하지 않은 상태로 create로 접근한다면 login 창으로 넘어간다.
def create(request):
    # 데코레이터를 사용하지 않는 경우
    if not request.user.is_authenticated:       # 인증되지 않은 유저가 create에 접근한다면
        return redirect('accounts:login')       # 로그인 창으로 보내버리기

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid:
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
