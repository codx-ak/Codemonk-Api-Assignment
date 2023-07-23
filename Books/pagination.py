from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 1

class CustomPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'Next page': self.get_next_link(),
                'Current page': int(self.request.GET.get('page', DEFAULT_PAGE)), # can not set default = self.page
                'Previous page': self.get_previous_link()
            },
            'Total Books': self.page.paginator.count,
            'Page size': int(self.request.GET.get('page_size', self.page_size)),
            'results': data
        })