from django.urls import path
from .views import index,contact,log_in,logout_view



urlpatterns = [
    path('',index,name='index'),
    path('contact/',contact,name='contact'),
    path('login/',log_in,name="log_in"),
    path('logout',logout_view,name='logout'),
]