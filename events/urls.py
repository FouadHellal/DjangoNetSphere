from . import views
from django.urls import path

urlpatterns = [

    #path('',views.home_temp,name='home'),
    path('Iotgauge/', views.home_temp, name='get_latest_data'),
    path('trigger_topology/', views.trigger_topology_commands, name='trigger_topology'),

]
#<int:year>/<str:month> the path converters
