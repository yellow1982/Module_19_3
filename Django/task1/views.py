from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def sign_up_by_html(request):
    Buyers = Buyer.objects.all()
    info = {}
    context = {'info': info,}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        for buyer in Buyers:
            if username == buyer.name:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'registration_page.html', context)

        if password == repeat_password and int(age) >= 18:
            Buyer.objects.create(name=username, balance=10000, age=age)
            return HttpResponse(f'Приветсвуем, {username}')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
    return render(request, 'registration_page.html', context)





def main_page(request):
    return render(request, 'platform.html')

def games(request):

    games = Game.objects.all()
    context = {
        'games': games,

    }
    return render(request, 'games.html', context)

def cart(request):
    return render(request, 'cart.html')

def menu(request):
    return render(request, 'menu.html')



