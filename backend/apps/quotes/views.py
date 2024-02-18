from rest_framework import generics
from apps.quotes.models import Quote
from apps.quotes.permissions import IsAdminOrReadOnly
from apps.quotes.serializers import QuoteSerializer


class QuoteListView(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminOrReadOnly]


class QuoteReadUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminOrReadOnly]
