from django.urls import path
from apps.quotes.views import (QuoteListView,
                               QuoteReadUpdateDestroyView)

urlpatterns = [
    path('quotes/', QuoteListView.as_view(), name="quote-list"),
    path('quotes/<int:pk>/', QuoteReadUpdateDestroyView.as_view(), name="quote-detail-view"),
]
