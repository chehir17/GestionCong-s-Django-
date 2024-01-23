from django.urls import path

from . import views

app_name = 'conversation'

urlpatterns = [
    path('', views.conver, name='conver'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/<int:user_pk>/', views.new_conversation, name='new'),
    path('<int:pk>/delete/', views.deleteconv, name='deleteconv'),

]