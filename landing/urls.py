from django.urls import path
from .views import index_view, MyTempView, template_view

app_name = 'landing'

urlpatterns = [
    # TODO добавьте здесь маршрут для вашего обработчика отображения страницы приложения landing
path('', index_view, name='index'),
#path('template/', template_view, name='template'),
path('template/', MyTempView.as_view(), name='template'),

]

