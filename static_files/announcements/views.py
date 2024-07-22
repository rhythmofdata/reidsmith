from django.shortcuts import render

import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.shortcuts import render, redirect
from .models import Announcement
from .forms import  AnnouncementForm, AnnouncementFormAdmin
from django.http import HttpResponseRedirect, HttpResponse
import csv
from django.contrib import messages
from django.db.models import Q

# Import Pagination tools
from django.core.paginator import Paginator



# Create your views here.




def announcements_home(request):
    announcement_list = Announcement.objects.all().order_by('announcement_date')  #Grab all of the announcement
    return render(request, 'announcements_home.html',
                  {'announcement_list': announcement_list})


def add_announcement(request):
    submitted = False
    if request.method == "POST":
        if request.user.is_superuser:
            form = AnnouncementFormAdmin(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/add_announcement?submitted=True')
        else:
            form = AnnouncementForm(request.POST)
            if form.is_valid():
                announcement = form.save(commit=False)
                announcement.manager = request.user #logged in
                announcement.save()
            
                return HttpResponseRedirect('/add_announcement?submitted=True')
    else:
        #just going to the page, not submitting
        if request.user.is_superuser:
            form = AnnouncementFormAdmin
        else:
            form = AnnouncementForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_announcement.html',{'form':form,'submitted':submitted})


def list_announcements(request):
    announcement_list = Announcement.objects.all().order_by('announcement_date')  #Grab all of the events
    return render(request, 'announcement_list.html',
                  {'announcement_list': announcement_list})

'''

def all_events(request):
    event_list = Event.objects.all().order_by('event_date')  #Grab all of the events
    return render(request, 'event_list.html',
                  {'event_list': event_list})
    

def update_event(request,event_id): # Grabbing specific items
    event = Event.objects.get(pk=event_id)
    if request.user.is_superuser:
        form = EventFormAdmin(request.POST or None, instance=event)
    else:
        form = EventForm(request.POST or None, instance=event)

    if form.is_valid():
        form.save()
        return redirect('list-events')

    return render(request, 'update_event.html',
                  {'event': event, 'form':form})


def delete_event(request,event_id):
    event = Event.objects.get(pk=event_id)
    if request.user == event.manager:
        event.delete()
        messages.success(request,('Event Deleted!'))
        return redirect('list-events')
    else:
        messages.success(request,('You are not authorized to delete this event!  Please contact admin or owner of event.'))
        
        return redirect('list-events')

def delete_venue(request,venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venues')
        





#These are events the user will be attending
def my_events(request):
    if request.user.is_authenticated:
        me = request.user.id
        events = Event.objects.filter(attendees=request.user.id)  #could use me instead of request.user.id
        return render(request, 'my_events.html',{"events":events})
    
    else:
         messages.success(request,('You are not authorized to view this event! Please login.'))
         return redirect('home')
    



def search_events(request):
    if request.method == "POST":
        searched = request.POST['searched']
        #events = Event.objects.filter(description__contains=searched | name__contains=searched)
        
        events= Event.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))

        return render(request, 'search_events.html',
        {'searched':searched,'events':events})
    else:
        return render(request, 'search_events.html',
        {})


'''