from django.urls import path
from .views import*

urlpatterns = [
    path('',index,name='index'),
    path('add/',add,name='add'),
    path('delete/',delete,name='delete'),
    path('edit/',edit,name='edit')
]