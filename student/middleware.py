import time
from django.db import connection


CONTENT_TYPES = ('text/html', 'application/xhtml+xml')


class QueryTimeMiddlewareShow(object):

    def process_request(self, request):
        self._start_time = time.time()

    def process_response(self, request, response):
        query_time = time.time() - self._start_time
        numbers_query = len(connection.queries)
        text_request = "Время запросов: %s, количество запросов: %s<br />" % (query_time, numbers_query)

        for i in connection.queries:
            text_request += " запрос: %s<br />" % (i)

        if response.status_code == 200:
            response.content += bytes(text_request, 'utf-8')

        return response