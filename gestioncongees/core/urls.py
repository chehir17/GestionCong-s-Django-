from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views
from .views import custom_logout



app_name = 'core'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('listUser/', views.getUser, name='getUser'),
    path('adduser/', views.adduser, name='adduser'),
    path('logout/', custom_logout, name='custom_logout'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<int:pk>/editetat/', views.editstatus, name='editstatus'),
]