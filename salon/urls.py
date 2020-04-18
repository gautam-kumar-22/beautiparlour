from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('about/', views.AboutListView.as_view(), name='about'),
    path('service/', views.ServiceListView.as_view(), name='service'),
    path('gallery/', views.GalleryListView.as_view(), name='gallery'),
    path('contact-us/', views.ContactUsView.as_view(), name='contact-us'),
]
