from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('call_analysis/', views.call_analysis),

]
