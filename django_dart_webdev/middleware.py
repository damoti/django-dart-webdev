import re
import requests
from django.http import HttpResponse
from django.conf import settings


BASE_URL_REGEX = re.compile(b"var baseUrl = \(function \(\) {.*?}\(\)\);", re.DOTALL)


class ProxyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.get_full_path()
        if path.startswith(settings.DART_URL):
            path = path[len(settings.DART_URL):]
            proxy_response = requests.request(request.method, f'{settings.WEBDEV_URL}/{path}')
            content = proxy_response.content
            if path.endswith('.dart.js') or path.endswith('dart.bootstrap.js'):
                content = BASE_URL_REGEX.sub(f'var baseUrl = "{settings.DART_URL}";'.encode(), content)
            return HttpResponse(content, status=proxy_response.status_code)

        return self.get_response(request)
