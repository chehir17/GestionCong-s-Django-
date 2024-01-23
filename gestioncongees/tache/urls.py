from django.urls import path
from . import views

app_name = 'tache'

urlpatterns = [
    path('tache_list/', views.ListTache, name='ListTache'),
    path('addTache/', views.addTache, name='addTache'),
    path('<int:pk>/edit/', views.editTache, name='editTache'),
    path('<int:pk>/delete/', views.deleteTache, name='deleteTache'),

]