from django.urls import path
from .views import LeadsListView, lead_list

app_name = "leads"

urlpatterns = [
    #path('', LeadsListView.as_view(), name='lead_list'),
    path('', lead_list, name='lead_list'),

    
]
