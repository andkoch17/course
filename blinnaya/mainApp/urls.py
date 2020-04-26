from django.urls import path, include

from . import views

app_name = 'mainApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('make_order', views.make_order, name='make_order'),
    path('wait/<order_id>', views.wait, name='wait')
]