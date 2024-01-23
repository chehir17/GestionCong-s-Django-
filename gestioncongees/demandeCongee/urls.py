from django.urls import path
from . import views

app_name = 'demandeCongee'

urlpatterns = [
    path('<int:pk>/demandeCong/', views.d_Congee, name='d_Congee'),
    path('listc/', views.ListConges, name='ListConges'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/editstat/', views.editstatus, name='editstatus'),
    path('<int:pk>/delete/', views.delete, name='delete')

]