from django.shortcuts import render
import random

# Create your views here.
def index(request):
    context = {'name': "규훈!"}
    return render(request, 'articles/index.html', context)

def dinner(request):
    foods = ['국밥', '국수', '카레', '삼겹살']
    picked = random.choice(foods)
    context = {             # 딕셔너리 형태로 html로 전송
        'foods': foods,      # 이름 굳이 맞출 필요 없다.
        'picked': picked,
    }
    return render(request, 'articles/dinner.html', context)


# fake naver
def search(request):
    return render(request, 'articles/search.html')


# throw & catch
def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    print(request)
    print(type(request))
    print(request.GET)
    print(request.GET.get('message'))       # 딕셔너리. key값을 가져오면 throw에서 보낸 value를 받을 수 있다.
    # 1. 사용자로부터 요청을 받아서
    # 2. 요청에서 사용자 입력 데이터를 찾아
    # 3. context에 저장 후 catch 템플릿에 출력
    message = request.GET.get('message')
    context = {'message': message}
    return render(request, 'articles/catch.html', context)


# URLs

def greeting(request, name):
    context = {
        'name': name,            # url에 있는 변수를 받은 것이다.
                                # 만약 같은 변수가 여러개라면, url이 우선 순위가 된다.
    }
    return render(request, 'articles/greeting.html', context)

def detail(request, num):
    context = {
        'num': num,
    }
    return render(request, 'articles/detail.html', context)