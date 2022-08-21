from django.shortcuts import HttpResponse

def index(request):    
    return HttpResponse('Главная страница')


def group_posts(request,pk):
    return HttpResponse('Посты, отфильтрованные по группам')
