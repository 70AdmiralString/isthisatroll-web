from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('<str:pk>/', views.DetailView.as_view(), name='detail'),
    path('', views.search, name='search')
]
