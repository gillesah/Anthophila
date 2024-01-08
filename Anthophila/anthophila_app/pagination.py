from rest_framework import pagination


class MyPagination(pagination.PageNumberPagination):
    page_size = 2
    max_page_size = 1000
    page_size_query_param = 'page_size'
