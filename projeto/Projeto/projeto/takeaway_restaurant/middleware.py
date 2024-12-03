from django.shortcuts import redirect

class VerificarPermissoesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and not request.user.groups.filter(name='Clientes').exists():
            return redirect('homepage')
        response = self.get_response(request)
        return response