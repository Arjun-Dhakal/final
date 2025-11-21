from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path("slides/", slide_list, name='slide_list'),
    path("create/", slide_create, name='slide_create'),
    path("update/<int:pk>/", slide_update, name='slide_update'),
    path("delete/<int:pk>/", slide_delete, name='slide_delete'),
    path('aboutus/', aboutus_list, name='aboutus_list'),
    path('aboutus/create/', aboutus_create, name='aboutus_create'),
    path('aboutus/update/<int:pk>/', aboutus_update, name='aboutus_update'),
    path('aboutus/delete/<int:pk>/', aboutus_delete, name='aboutus_delete'),
    path('contact/', contactus_list, name='message'),
    
    path('media/', media_list, name='media'),
    path('media/create/', media_create, name='media_create'),
    path('media/update/<int:pk>/', media_update, name='media_update'),
    path('media/delete/<int:pk>/', media_delete, name='media_delete'), 
    
    path('services/', service_list, name='service'),
    path('services/create/', service_create, name='service_create'),    
    path('services/update/<int:pk>/', service_update, name='service_update'),
    path('services/delete/<int:pk>/', service_delete, name='service_delete'), 
]
