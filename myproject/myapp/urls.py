from django.urls import path
from . import views
app_name='myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"),
]