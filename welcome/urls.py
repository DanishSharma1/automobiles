from django.contrib import admin
from django.urls import include, path
from.import views
'''
urlpatterns = [
    path('django/', include('welcome.urls')),
]
'''
urlpatterns = [
    path('index/', views.index),
    path('index/car/django/index/', views.index),
    path('index/car/sell/', views.sell),
    path('index/sell/django/index/car/', views.car),
    path('car/', views.car),
    path('index/car/sell/django/index/car/', views.car),
    path('index/car/', views.car, name="car"),
    path('index/car/add/',views.add,name="add"),
    path('index/car/add/addrecord/',views.addrecord,name="addrecord"),
    path('index/car/delete/<int:id>',views.delete,name='delete'),
    path('index/car/update/<int:id>',views.update,name="update"),
    path('index/car/update/updaterecord/<int:id>',views.updaterecord,name="udpaterecord"),
    path('index/car/sell/django/index/car/sell/',views.sell),
    path('index/sell/', views.sell),
    path('index/contact/',views.contact),
    path('index/contact/sell/', views.sell),
    path('index/contact/sell/django/index/car/', views.car),
    path('index/sell/contact/', views.contact),
    path('index/sell/django/index/car/contact/',views.contact),
    path('index/car/contact/',views.contact),
    path('index/car/sell/contact/',views.contact),
    path('index/car/sell/contact/sell/', views.sell),
    path('index/car/sell/contact/sell/django/index/car/',views.car),
    path('index/sell/contact/sell/', views.sell),
    path('index/sell/contact/sell/django/index/car/',views.car),
    path('index/car/contact/sell/',views.sell),
    path('index/car/contact/sell/django/index/car/',views.car),
    path('index/contact/car/',views.car),
    path('index/contact/index',views.index),
    path('index/car/contact/car/',views.car),
    path('index/car/contact/car/add/',views.add),
    path('index/car/contact/car/add/addrecord/',views.addrecord),
    path('index/car/fill/', views.fill),
    path('index/car/sell/contact/car/',views.car),
    path('index/car/contact/car/fill/',views.fill),
    path('index/car/contact/car/sell/',views.sell)


]