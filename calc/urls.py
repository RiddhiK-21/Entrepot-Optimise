from django.urls import path
from django.contrib import admin
from . import views

urlpatterns=[
path('',views.home,name="home"),
#path('', views.button),
#path('output/', views.output,name="script"),
#path('calc/external/', views.external),

]