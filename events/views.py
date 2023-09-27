from django.shortcuts import render, redirect
from django.db.models import Q  #to search
from django.http import HttpResponse
import csv #to generate csv file

#import below to generate PDF file after installing 'pip install reportlab'
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


# Create your views here.
from .models import Event, Venue
from .forms import VenueForm, EventForm

def event_list(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html', {
        'event_list': event_list,
    })

def event_detail(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render(request, 'events/event_detail.html', {
        'event': event, 
    })

#function for create Venue form
def add_venue(request):
    submitted = False 
    venues = Venue.objects.all()
    if request.method == 'POST':
        form = VenueForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/add_venue?submitted=True')
    else:
        form = VenueForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html', {
        'form': form,
        'submitted': submitted,
        'venues': venues,
    })

def list_venue(request):
    venues = Venue.objects.all()
    return render(request, 'events/list_venue.html',{
        'venues': venues,
    })

def add_event(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    return render(request, 'events/add_event.html', {
        'form': form, 
    })

#updating an event 
def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(instance=event)
    if request.method =="POST":
        form = EventForm(request.POST or None, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    return render(request, 'events/update_event.html',{
        'form': form, 
    })

#to delete an event
def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.method =="POST":
        event.delete()
        return redirect ('event_list')
    return render(request, 'events/delete_event.html', {
        'event': event,
    })

#search bar function
def search_event(request):
    query = request.GET.get('q')
    query_list_event = Event.objects.all()
    query_list_venue = Venue.objects.all()
    if query is not None:
        lookups = Q(name__icontains=query)
        query_list_event = Event.objects.filter(lookups) 
        query_list_venue = Venue.objects.filter(lookups)
    return render(request, 'events/search_event.html',{
        'event': query_list_event,
        'venue': query_list_venue,
    })

#download text file
def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition']= 'attachement;filename=venues.txt'
    venues = Venue.objects.all()
    line = []
    for venue in venues:
        line.append(f'Name:{venue.name}\nAddress: {venue.address}\n\n\n')
    
    response.writelines(line)
    return response

#download csv file  (import CSV)
def download_venue_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;filename=venues.csv'

    writer = csv.writer(response)

    venues = Venue.objects.all()

    writer.writerow(['Name', 'Address','Zip Code','Phone','Email','Website'])

    for venue in venues:
        writer.writerow([venue.name,venue.address, venue.zip_code, venue.phone, venue.email_address, venue.web,])

    return response 

#download pdf file
def download_venue_pdf(request):
    #creating Bytestream buffer
    buf = io.BytesIO()
    #creating canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    #creating a text object
    textobj=c.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont('Helvetica', 14)

    venues = Venue.objects.all()
    lines = []
    for venue in venues:
        lines.append(f'Name:{venue.name}')
        lines.append(f'Address:{venue.address}')
        lines.append(f'---------------')

    for line in lines:
        textobj.textLine(line)

    c.drawText(textobj)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='venue.pdf')

"""

def add_event(request):
    return render(request, 'events/add_event.html', {
        
    })

"""