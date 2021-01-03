from django.urls import path

from . import views

app_name = 'audits'      # namespace

urlpatterns = [
    path('', views.index, name='index'),
    path('client/', views.client, name='client'),
    path('client/<int:pk>', views.clientDetail, name='client-detail'),
    path('site/', views.allSite, name='all-site'),
]