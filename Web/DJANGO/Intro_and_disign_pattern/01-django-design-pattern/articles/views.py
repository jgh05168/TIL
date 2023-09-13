from django.shortcuts import render     # render 페이지 생성

# Create your views here.
def index(request):
    # 메인 페이지를 응답
    # articles/templates에 있는 articles를 불러오는 것이다. 혼동 주의
    return render(request, 'articles/index.html')       # render(요청, 템플렛 경로)