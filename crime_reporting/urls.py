from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('call_analysis/', views.CallAnalysis.as_view(), name='call_analysis'),

]
