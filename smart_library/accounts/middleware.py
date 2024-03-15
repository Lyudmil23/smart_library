from django.shortcuts import render


class Custom404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            user = request.user
            profile = getattr(user, 'profile', None)
            return render(request, '404.html', {'profile': profile}, status=404)
        return response
