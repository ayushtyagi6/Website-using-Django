from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index ,name='index'), 
    path('post/<str:slug>',views.post ,name='post'),
    path('add',views.add ,name='add'),
    
    
]