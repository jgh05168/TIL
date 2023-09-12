from django.shortcuts import render     # render 페이지 생성

# Create your views here.
def index(request):
    # 메인 페이지를 응답
    return render(request, 'articles/index.html')       # render(요청, 템플렛 경로)