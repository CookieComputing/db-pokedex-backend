"""
Helper modules that handle various operations regarding HTTP requests and responses
"""

from django.http import HttpRequest, Http404

def assert_post(request: HttpRequest) -> None:
    if request.method != 'POST':
        raise Http404("Expected POST request")