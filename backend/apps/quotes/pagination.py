from rest_framework.pagination import PageNumberPagination


class TinyPagination(PageNumberPagination):
    page_size = 3
