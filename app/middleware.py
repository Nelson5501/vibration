# myapp/middleware.py
import datetime
from app.models import Visitor

class VisitorTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if not request.user.is_staff:
            Visitor.objects.create(
                path=request.path,
                ip_address=request.META['REMOTE_ADDR'],
                timestamp=datetime.datetime.now()
            )
        return response
