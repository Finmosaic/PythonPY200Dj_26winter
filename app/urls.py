from django.urls import path, include
from .views import template_view, index_view, login_view, register_view, \
    logout_view, user_detail_view, get_text_json, MyTemplView, MyTemplateView, MyFormView, MyLoginView, LoginView
from django.contrib.auth import views as auth_views
app_name = 'app'

urlpatterns = [
    path('', index_view, name='index'),
    path('template/', MyFormView.as_view(), name='template'),
    #path('template/', MyTemplateView.as_view(), name='template'),
    #path('template/', MyTemplView.as_view(), name='template'),
    #path('template/', template_view, name='template'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True, template_name='app/login.html'), name='login'),
    #path('login/', MyLoginView.as_view(), name='login'),
    #path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout', logout_view, name='logout'),
    path('profile/', user_detail_view, name='user_profile'),
    path('get/text/', get_text_json),


]






















