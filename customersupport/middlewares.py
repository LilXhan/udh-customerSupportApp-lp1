from django.conf import settings
from django.http import JsonResponse

class ApiKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        api_key = request.headers.get('API-KEY')
        if api_key != settings.API_KEY:
            return JsonResponse({'error': 'Invalid API Key'}, status=403)
        return self.get_response(request)