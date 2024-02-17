from django.urls import path
from apps.quotes.views import QuoteList

urlpatterns = [
    path('quotes/', QuoteList.as_view(), name="quote-list"),
]
