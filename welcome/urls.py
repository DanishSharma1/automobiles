from django.contrib import admin
from django.urls import include, path
from.import views
'''
urlpatterns = [
    path('django/', include('welcome.urls')),
]
'''
urlpatterns = [
    path('', views.index),
    path('car/', views.index),
    path('car/sell/', views.sell),
    path('sell/car/', views.car),
    path('car/', views.car),
    path('car/sell/car/', views.car),
    path('car/', views.car, name="car"),
    path('car/add/',views.add,name="add"),
    path('car/add/addrecord/',views.addrecord,name="addrecord"),
    path('car/delete/<int:id>',views.delete,name='delete'),
    path('car/update/<int:id>',views.update,name="update"),
    path('car/update/updaterecord/<int:id>',views.updaterecord,name="udpaterecord"),
    path('car/sell/car/sell/',views.sell),
    path('sell/', views.sell),
    path('contact/',views.contact),
    path('contact/sell/', views.sell),
    path('contact/car/', views.car),
    path('sell/contact/', views.contact),
    path('sell/car/contact/',views.contact),
    path('car/contact/',views.contact),
    path('car/sell/contact/',views.contact),
    path('car/sell/contact/sell/', views.sell),
    path('car/sell/contact/sellcar/',views.car),
    path('sell/contact/sell/', views.sell),
    path('sell/contact/sell/car/',views.car),
    path('car/contact/sell/',views.sell),
    path('car/contact/sell/car/',views.car),
    path('contact/car/',views.car),
    path('contact/',views.index),
    path('car/contact/car/',views.car),
    path('car/contact/car/add/',views.add),
    path('car/contact/car/add/addrecord/',views.addrecord),
    path('car/fill/', views.fill),
    path('car/sell/contact/car/',views.car),
    path('car/contact/car/fill/',views.fill),
    path('car/contact/car/sell/',views.sell)


]