from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('category/<slug:slug>/', views.category_list, name='category_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('contact/thanks/', views.contact_thanks, name='contact_thanks'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
]
