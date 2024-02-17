from rest_framework import generics
from apps.quotes.models import Quote
from apps.quotes.permissions import IsAdminOrReadOnly
from apps.quotes.serializers import QuoteSerializer


class QuoteList(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminOrReadOnly]
