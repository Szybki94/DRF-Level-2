from django.urls import path
from apps.quotes.views import QuoteListView

urlpatterns = [
    path('quotes/', QuoteListView.as_view(), name="quote-list"),
]
