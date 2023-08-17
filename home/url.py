from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='home'),
    path('index',views.index, name='Home'),
    path('about',views.about, name='about'),
    # path('service',views.service, name='service'),
    path('contect',views.contect, name='contect'),
    path('help',views.help, name='help'),
]
