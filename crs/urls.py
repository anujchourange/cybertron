from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='crs-home'),
    path('about/', views.about, name='crs-about'),

]
