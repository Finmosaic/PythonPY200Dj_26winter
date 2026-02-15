from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from landing.forms import TemplateForm


# Create your views here.


class MyTempView(View):
    def get(self, request):
        return render(request, 'landing/index.html')

    def post(self, request):
        received_data = request.POST  # Приняли данные в словарь
        form = TemplateForm(received_data)  # Передали данные в форму

        if form.is_valid():  # Проверили, что данные все валидные
            my_name = form.cleaned_data.get("my_name")  # Получили очищенные данные
            my_subject = form.cleaned_data.get("my_subject")
            my_email = form.cleaned_data.get("my_email")
            my_message = form.cleaned_data.get("my_message")
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # Получение IP
            else:
                ip = request.META.get('REMOTE_ADDR')  # Получение IP

            user_agent = request.META.get('HTTP_USER_AGENT')

            return JsonResponse(data=[my_name, my_subject, my_email, my_message, ip, user_agent],
                                safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
        return render(request, template_name='landing/index.html', context={'form': form})







def template_view(request):
    if request.method == "GET":
        return render(request, 'landing/index.html')

    if request.method == "POST":
        received_data = request.POST  # Приняли данные в словарь
        my_name = received_data.get('my_name')
        my_email = received_data.get('my_email')
        my_subject = received_data.get('my_subject')
        return JsonResponse(data={'name': my_name, 'email': my_email, 'subject': my_subject},
                                 json_dumps_params={'ensure_ascii':False})

        # как пример получение данных по ключу `my_text`
        # my_text = received_data.get('my_text')


    # if request.method == "POST":
    #     form = TemplateForm(request.POST)
    #         if form.is_valid():

def index_view(request):
    if request.method == "GET":
        return render(request, 'landing/index.html')


