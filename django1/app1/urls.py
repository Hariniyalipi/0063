from django.urls import path
from  . import views
urlpatterns=[ 
    path('fact/',views.fact,name="fact"),
    path('sq/',views.square,name="square"),
    path('fact1/',views.factorial,name="fact1"),
    path('factorial/',views.factorial_input,name="factorial"),
    path('string/',views.index,name="index"),
    ]