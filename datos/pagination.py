from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    page_size = 15
    max_page_size = 100
    page_query_param = 'page'

    def get_paginated_response(self, data):
        
        from rest_framework.response import Response
        import math

        total_pages = math.ceil(self.page.paginator.count / self.get_page_size(self.request))
        return Response ({
            'totalItems' : self.page.paginator.count,
            'totalPaginas' : total_pages,
            'paginaActual' : self.page.number,
            'data' : data   
         })