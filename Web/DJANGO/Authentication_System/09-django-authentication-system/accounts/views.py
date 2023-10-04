from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login     # 로그인을 가능하게 해주는 내장 라이브러리
from django.contrib.auth import logout as auth_logout   # 로그아웃을 가능하게 해주는 내장 라이브러리
# Create your views here.

# 로그인
def login(request):
    if request.method == 'POST':       
        # 세션 create 가 이루어지는 곳
        form = AuthenticationForm(request, request.POST)        # models와 다르게 인자의 순서가 다르다.(주의) | 인자 순서 : (request, data)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())        # session create, id 발급
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


# 로그아웃
def logout(request):
    auth_logout(request)
    return redirect('articles:index')