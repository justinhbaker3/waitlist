from django.urls import path

from . import views

app_name='waitlist'
urlpatterns = [
    path('', views.index, name='index'),
    path('join/', views.join, name='join'),
    path('waiter/<str:username>/', views.getWaiter, name='get-waiter')
]
