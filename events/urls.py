
from django.urls import path, include
from . import views
#from .views import StripeWebhookView
#from .views import CancelView, SuccessView
#from .views import CreateStripeCheckoutSessionView
from .views import (
    EventDetailView,
    EventListView,
)
#from .views import StripeWebhookView

# See docs.python.org for datetime and other functionalities

app_name = "events"

urlpatterns = [
    # int: numbers
    # str: string
    # path: whole urls /  
    # slug: hyphen- and _ underscores  etc
    # uuid: universally unique identifier


    path('events/', views.events_home, name="events_home"),
    #path('event-ticket-purchase', views.event_ticket_purchase,name='event_ticket_purchase'),
    #path('<int:year>/<str:month>/', views.events_home, name="events_home"),
    path('event-list',views.all_events, name="list-events"),
    path('event-details',views.event_details, name="event-details"),
    path('add_venue',views.add_venue, name="add-venue"),
    path('list_venues',views.list_venues, name="list-venues"),
    path('show_venue/<venue_id>',views.show_venue, name='show-venue'),
    path('search_venues',views.search_venues, name='search-venues'),
    path('update_venue/<venue_id>',views.update_venue, name='update-venue'),
    path('add_event',views.add_event, name="add-event"),
    path('update_event/<event_id>',views.update_event, name='update-event'),
    path('delete_event/<event_id>',views.delete_event, name='delete-event'),
    path('delete_venue/<venue_id>',views.delete_venue, name='delete-venue'),
    path('venue_text',views.venue_text,name='venue-text'),
    path('venue_csv',views.venue_csv,name='venue-csv'),
    path('my_events',views.my_events,name='my-events'),
    path('search_events',views.search_events,name='search-events'),
    path('admin_approval',views.admin_approval,name='admin-approval'),
    path("event-list",EventListView.as_view(),name="event-list"),
    path("<int:pk>/",EventDetailView.as_view(), name="event-details"),
    

]


'''
    path(
        "create-checkout-session/<int:pk>/",
        CreateStripeCheckoutSessionView.as_view(),
        name="create-checkout-session",
    )'''

#path("success/",SuccessView.as_view(), name="success"),
#path("cancel/",CancelView.as_view(), name="cancel"),
#path("webhook/", StripeWebhookView.as_view(), name="stripe-webhook"),