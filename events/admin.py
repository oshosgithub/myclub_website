from django.contrib import admin

# Register your models here.
from .models import (
    Venue, 
    MyClubUser,
    Event,
)


#admin.site.register(Venue)
admin.site.register(MyClubUser)
#admin.site.register(Event)

#to change Admin page for Model Venue
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone',)
    ordering = ('name',) 
    #this will order name attributes in alphabetecal order. Putting ('-name',) will do reverse. 
    search_fields = ('name', 'address',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'venue', 'event_date', 'manager', 'attendees', 'description',)
    list_display = ('name', 'event_date',)
    ordering = ('event_date',)
    list_filter = ('manager', 'name', 'attendees',)