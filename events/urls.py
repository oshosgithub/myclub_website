from django.urls import path 
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event_detail/<event_id>/', views.event_detail, name='event_detail'),
    path('add_event/', views.add_event, name='add_event'),
    path('update_event/<event_id>/', views.update_event, name='update_event'),
    path('delete_event/<event_id>/', views.delete_event, name='delete_event'),
    path('search_event/', views.search_event, name='search_event'),
    path('add_venue/', views.add_venue, name='add_venue'),
    path('list_venue/', views.list_venue, name='list_venue'),
    path('download_venue_text/', views.venue_text, name='download_venue_text'),
    path('download_venue_csv/', views.download_venue_csv, name='download_venue_csv'),
    path('download_venue_pdf/', views.download_venue_pdf, name='download_venue_pdf'),
]