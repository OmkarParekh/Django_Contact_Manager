from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact,name='Contactlist'),
    path('add/', views.addcontact,name='Contactadd'),
    path('add/d/<int:id>', views.delete,name='DeleteContact'),
    path('add/e/<int:id>', views.edit,name='EditContact'),
]
