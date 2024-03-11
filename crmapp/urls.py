from django.urls import path
from .import views  


urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('archive', views.archive, name='archive'),
    path('contact',views.contact,name='contact'),
    path('pricing',views.pricing,name='pricing'),
    path('signup',views.signup,name='signup'),
    


]