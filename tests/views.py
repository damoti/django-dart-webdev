from django.http import HttpResponse


def index(request):
    return HttpResponse(
        """
        <html>
            <head><script defer src="/dart/main.dart.js"></script></head>
            <body id="output">Hi!</body>
        </html>
        """
    )
