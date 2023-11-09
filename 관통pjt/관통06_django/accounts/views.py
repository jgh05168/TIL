from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_http_methods

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here

# 로그인
require_http_methods(['GET','POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('boards:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('boards:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/login.html',context)


# 로그아웃
@login_required
def logout(request):
    auth_logout(request)
    return redirect('boards:index')


# 회원가입
require_http_methods(['GET','POST'])
def signup(request):

    if request.user.is_authenticated:
        return redirect('boards:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('boards:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/signup.html',context)


# 회원탈퇴
@login_required
def delete(request):
    request.user.delete()
    return redirect('boards:index')


# 프로필
@login_required
def profile(request,username):
    person = get_object_or_404(get_user_model(),username=username)
    context = {
        'person':person,
    }
    return render(request, 'accounts/profile.html',context)


# 팔로잉, 팔로우
@login_required
def follow(request,user_pk):
    
    person = get_object_or_404(get_user_model(),pk=user_pk)
    if person != request.user:
        if request.user in person.followers.all():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return redirect('accounts:profile', person.username)

