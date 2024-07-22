from django.urls import path

from .views import StripeWebhookView
from .views import CancelView, SuccessView
from .views import CreateStripeCheckoutSessionView
from .views import (
    ProductDetailView,
    ProductListView,
)
from .views import StripeWebhookView

app_name = "payments"

urlpatterns = [
    path("product-list",ProductListView.as_view(),name="product-list"),
    path("<int:pk>/",ProductDetailView.as_view(), name="product-detail"),
    path(
        "create-checkout-session/<int:pk>/",
        CreateStripeCheckoutSessionView.as_view(),
        name="create-checkout-session",
    ),
    path("success/",SuccessView.as_view(), name="success"),
    path("cancel/",CancelView.as_view(), name="cancel"),
    path("webhook/", StripeWebhookView.as_view(), name="stripe-webhook"),

]