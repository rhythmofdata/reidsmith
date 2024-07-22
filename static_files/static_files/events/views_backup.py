import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.shortcuts import render, redirect
from .models import Event, Venue
from .forms import VenueForm, EventForm
from django.http import HttpResponseRedirect, HttpResponse



# Create your views here.


def all_events(request):
    event_list = Event.objects.all().order_by('event_date')  #Grab all of the events
    return render(request, 'event_list.html',
                  {'event_list': event_list})

def events_home(request, year=datetime.now().year , month=datetime.now().strftime('%B')):
    name = "Hodges"
    month = month.capitalize()
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # create a calendar
    cal = HTMLCalendar().formatmonth(
        year,
        month_number)
    
    #Get current year
    now = datetime.now()
    current_year = now.year

    # get current time
    time  = now.strftime('%I:%M: %p')
    
    return render(request,'events_home.html')
'''return render(request,
        'events_home.html',{
        "name": name,
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
        "time": time,
    })'''
    


def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_venue.html',{'form':form,'submitted':submitted})


def list_venues(request):
     venue_list = Venue.objects.all().order_by('name') #Grab all of the events Use ? to randomize
     return render(request, 'venue.html',
                  {'venue_list': venue_list})


def show_venue(request,venue_id): # Grabbing specific items
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'show_venue.html',
                  {'venue': venue})



def search_venues(request):
    if request.method == "POST":
        searched = request.POST.get('searched',False)
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'search_venues.html',
        {'searched':searched,'venues':venues})
    else:
        return render(request, 'search_venues.html',
        {})
    

def update_venue(request,venue_id): # Grabbing specific items
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list-venues')

    return render(request, 'update_venue.html',
                  {'venue': venue, 'form':form})
        





def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_event.html',{'form':form,'submitted':submitted})


def update_event(request,event_id): # Grabbing specific items
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')

    return render(request, 'update_event.html',
                  {'event': event, 'form':form})


def delete_event(request,event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('list-events')

def delete_venue(request,venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venues')
        

# generate a Text file Venue list
def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=venues.txt'
    # Designate the model
    venues = Venue.objects.all()

    # Loop through venues
    # create blank list
    lines = []
    #loop thru and output
    for venue in venues:
        lines.append(f'{venue}\n{venue.address}\n{venue.zip_code}\n')


    #write to text file
    response.writelines(lines)
    return response
