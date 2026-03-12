from django.shortcuts import render, redirect
from django.contrib import messages
from apps.base.models import Foods, Category_food, About_us
import requests
import os

def reservation(request):
    categories = Category_food.objects.all()
    category_title = request.GET.get('category', '')
    food_title = request.GET.get('food', '')

    qs = Foods.objects.all()
    if category_title:
        qs = qs.filter(category__title__iexact=category_title)
    if food_title:
        qs = qs.filter(title__icontains=food_title)  # Можно поиск по части слова

    context = {
        'categories': categories,
        'food': qs,
        'selected_category': category_title,
        'selected_food': food_title,
    }
    return render(request, 'view/reservation.html', context)

def menu_food(request):
    foods = Foods.objects.all()
    return render(request, 'view/menu.html', {'foods': foods})


def about_us(request):
    about = About_us.objects.all()
    return render(request, 'view/about.html', {'about': about})

def home(request):
    return render(request, 'view/index.html')

def send_telegram_message(text):
    token = os.getenv('TELEGRAM_BOT_TOKEN', '7778964806:AAH1vN4h_IxT7z2epyNMfoqjYjIRzI4zNfc')
    chat_id = os.getenv('TELEGRAM_CHAT_ID', '5000264641')
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {'chat_id': chat_id, 'text': text}
    try:
        requests.post(url, data=data, timeout=10)
    except Exception as e:
        print(f"Error sending telegram message: {e}")

def reservation_submit(request):
    if request.method == 'POST':
        name = request.POST.get('fb_name')
        category = request.POST.get('category')
        food = request.POST.get('food')

        message = f"🥗 Новая заявка на заказ!\nИмя: {name}\nКатегория: {category}\nБлюдо: {food}"
        send_telegram_message(message)
        messages.success(request, "Ваш заказ успешно отправлен!")

        return redirect('reservation')
    else:
        return redirect('reservation')