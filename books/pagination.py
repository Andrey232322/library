from rest_framework.pagination import PageNumberPagination

class BooksPagination(PageNumberPagination):
    page_size = 20
    # page_size_query_param = 'page_size'  # Разрешаем менять размер страницы (опционально)
    # max_page_size = 100