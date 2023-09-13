from django.shortcuts import render

# Create your views here.
def hello(request, name):
    print(f"{name}")
    context = {'name': name,}
    return render(request, 'articles/hello.html', context)