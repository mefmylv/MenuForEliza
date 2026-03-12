from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of paths that don't require authentication
        exempt_paths = [
            reverse('admin:index') if 'admin' in request.path else None,
            # Add login/signup paths here if they exist
        ]
        
        # If the user is not authenticated and the path is not exempt, redirect to login
        # For now, let's just protect everything except admin
        if not request.user.is_authenticated and not request.path.startswith('/admin/'):
            return redirect(reverse('admin:login'))

        response = self.get_response(request)
        return response
