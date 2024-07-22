

import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.shortcuts import render, redirect
from .forms import VenueForm, EventForm, EventFormAdmin
import csv
from django.contrib import messages
from django.db.models import Q




from typing import Any
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView
from .models import EventPrice, Event, Order, Venue, EventPaymentHistory
from django.conf import settings
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
#import stripe
from django.core.mail import send_mail
# import get_object_or_404()
from django.shortcuts import get_object_or_404


#stripe.api_key = settings.STRIPE_SECRET_KEY

# Import Pagination tools
from django.core.paginator import Paginator



# Create your views here.

class EventListView(ListView):     #For Events to which tickets will be sold
    model = Event
    context_object_name ="events"
    template_name = "/templates/event_list.html"

class EventDetailView(DetailView):
    model = Event
    context_object_name =  "event"
    template_name = "event_details.html"

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data()
        context["prices"] = EventPrice.objects.filter(event_product=self.get_object())
        return context


def event_details(request):
    event_list = Event.objects.all().order_by('event_date')  #Grab all of the events
    return render(request, 'event_list.html',
                  {'event_list': event_list})


def all_events(request):
    event_list = Event.objects.all().order_by('event_date')  #Grab all of the events
    return render(request, 'event_list.html',
                  {'event_list': event_list})

def events_home(request):
    event_list = Event.objects.all().order_by('event_date')  #Grab all of the events
    return render(request, 'events_home.html',
                  {'event_list': event_list})
    


def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            venue = form.save(commit=False)
            venue.owner = request.user.id  #logged in user
            venue.save()
            #form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_venue.html',{'form':form,'submitted':submitted})







def list_venues(request):
     #venue_list = Venue.objects.all().order_by('name') #Grab all of the events Use ? to randomize
     venue_list = Venue.objects.all()

     # Set up pagination
     p = Paginator(Venue.objects.all(),4)
     page = request.GET.get('page')
     venues = p.get_page(page)


     return render(request, 'venue.html',
                  {'venue_list': venue_list,'venues':venues})


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
        if request.user.is_superuser:
            form = EventFormAdmin(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/add_event?submitted=True')
        else:
            form = EventForm(request.POST)
            if form.is_valid():
                event = form.save(commit=False)
                event.manager = request.user #logged in
                event.save()
            
                return HttpResponseRedirect('/add_event?submitted=True')
    else:
        #just going to the page, not submitting
        if request.user.is_superuser:
            form = EventFormAdmin
        else:
            form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_event.html',{'form':form,'submitted':submitted})


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


# generate a csv file Venue list
def venue_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=venues.csv'

    #Create a csv writer
    writer = csv.writer(response)

    # Designate the model
    venues = Venue.objects.all()

    # Add column headings to the csv file
    writer.writerow(['Venue Name','Address','Zip Code','Phone', 'Web Address','Email'])

    
    #loop thru and output
    for venue in venues:
        writer.writerow([venue.name, venue.address,venue.zip_code,venue.phone,venue.web,venue.email_address])


    
    return response

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
    


    
    



# Admin event approval view
def admin_approval(request):
    event_list = Event.objects.all().order_by("-event_date")
    if request.user.is_superuser:
        if request.method == "POST":
            id_list = request.POST.getlist('boxes')
            #This is hacky.  Figure out a way to make it more elegant
            event_list.update(approved=False)
            # Update the database
            for id in id_list:
                Event.objects.filter(pk=int(id)).update(approved=True)
            messages.success(request,"Event List Approval Has Been Updated")
            return redirect('list-events')


        else:
            return render(request,"admin_approval.html",{"event_list":event_list})
    else:
        messages.success(request,"You are not authorized to view this page.")
        return redirect('home')
    
    return render(request, 'admin_approval.html',{})



'''
class CreateStripeCheckoutSessionView(View):
    """
    Create a checkout session and redirect the user to Stripe's checkout page
    """

    def post(self, request, *args, **kwargs):
        price = EventPrice.objects.get(id=self.kwargs["pk"])

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": int(price.event_price) * 100,
                        "product_data": {
                            "name": price.event_product.name,
                            "description": price.event_product.description,
                            "images": [
                                f"{settings.BACKEND_DOMAIN}/{price.event_product.thumbnail}"
                            ],
                        },
                    },
                    "quantity": price.event_product.quantity,
                }
            ],
            metadata={"product_id": price.event_product.id},
            mode="payment",
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,
        )
        return redirect(checkout_session.url)
    
'''

'''
class CreateStripeCheckoutSessionView(View):
    """
    Create a checkout session and redirect the user to Stripe's checkout page
    """

    template_name = 'event_details.html'
    def get(self, request, *args, **kwargs):
        tickets = Event.objects.all()
        return render(request, self.template_name, {'tickets': tickets})
    

    def post(self, request, *args, **kwargs):
        ticket_ids = request.POST.getlist('tickets')
        tickets = Event.objects.filter(pk__in=ticket_ids)
        event_price = EventPrice.objects.get(id=self.kwargs["pk"])

        total_amount = sum(ticket.price for ticket in tickets)
        order = Order.objects.create(total_amount=total_amount)
        order.tickets.set(tickets)

        price = int(total_amount * 100)  # Convert to cents

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],


            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': f'Tickets - {", ".join(ticket.age_group for ticket in tickets)}',
                    },
                    'unit_amount': price,
                },
                'quantity': 1,
            }],
            #metadata={"product_id": price.event_product.id},
            mode="payment",
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,
        )
        return redirect(checkout_session.url)
'''
    




@method_decorator(csrf_exempt, name="dispatch")
class StripeWebhookView(View):
    """
    Stripe webhook view to handle checkout session completed event.
    """

    def post(self, request, format=None):
        payload = request.body
        endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
        sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
        event = None

        try:
            event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
        except ValueError as e:
            # Invalid payload
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError as e:
            # Invalid signature
            return HttpResponse(status=400)
       

        if event["type"] == "checkout.session.completed":
            print("Payment successful")
            
            session = event["data"]["object"]
            customer_email = session["customer_details"]["email"]
            product_id = session["metadata"]["product_id"]
            product = get_object_or_404(Event, id=product_id)
        

            send_mail(
                subject="Here is your product",
                message=f"Thanks for your purchase. The URL is: {event.url}",
                recipient_list=[customer_email],
                from_email="reunionsitetester@gmail.com",
            )
            EventPaymentHistory.objects.create(
                email=customer_email, event=event, payment_status="completed"
            ) # Add this

            payment_history = EventPaymentHistory.objects.create(
            email=customer_email, 
            event=event, 
            payment_status="completed")

            print(payment_history.payment_status)


        # Can handle other events here.

        return HttpResponse(status=200)
    


class SuccessView(TemplateView):
    template_name = "templates/success.html"




class CancelView(TemplateView):
    template_name = "templates/cancel.html"



def event_ticket_purchase(request):
    tickets = Event.objects.all()
    return render(request, "event_details.html", {'tickets': tickets})






