from django.urls import path
from .views import *

urlpatterns = [
    path('',home ,name='home'),
    path('dashboard/',dashboard,name='dashboard' ),
    path('category/',category,name='category' ),
    path('vehicleEntry/',vehicleEntry,name='vehicleEntry' ),
    path('managevehicle/',managevehicle,name='managevehicle' ),
    path('searchdata/',searchdata,name='searchdata' ),
    path('Account/',Account,name='Account' ),
    path('login1/',login1,name='login1' ),
    path('logout1/',logout1,name='logout1' ),
    path('categoryEntry/',categoryEntry,name='categoryEntry' ),
    path('vehicleEntryregister/',vehicleEntryregister,name='vehicleEntryregister' ),
    path('category/deactivate/<int:category_id>/',deactivate_category, name='deactivate_category'),
    path('category/delete/<int:category_id>/', delete_category, name='delete_category'),
    path('DoneBtn/<int:vehicleid>/', DoneBtn, name="DoneBtn"), 
    path('edit/<int:category_id>/', edit_category, name='edit'),

]