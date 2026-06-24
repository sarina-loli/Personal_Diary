from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register, name='register'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('profile/',views.profile,name='profile'),
    path('entry/add/',views.add_entry,name='add_entry'),
    path('entry/<int:pk>/',views.entry_detail,name='entry_detail'),
    path('entry/<int:pk>/edit/',views.edit_entry,name='edit_entry'),
    path('entry/<int:pk>/delete/',views.delete_entry,name='delete_entry'),
]