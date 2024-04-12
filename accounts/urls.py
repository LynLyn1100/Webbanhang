from django.urls import path, include
from accounts import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', views.Register.as_view(), name='register'),
    path('profile', views.profile, name='profile'),
    path('contact',views.contact, name='contact'),
    path('aboutus',views.aboutus, name='aboutus')

]
