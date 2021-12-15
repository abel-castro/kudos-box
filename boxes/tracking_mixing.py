import requests

from django.conf import settings


class TrackingMixin:
    def dispatch(self, request, *args, **kwargs):
        request_meta = {
            "HTTP_ACCEPT_LANGUAGE": request.META.get("HTTP_ACCEPT_LANGUAGE"),
            "HTTP_HOST": request.META.get("HTTP_HOST"),
            "HTTP_USER_AGENT": request.META.get("HTTP_USER_AGENT"),
            "HTTP_X_FORWARDED_FOR": request.META.get("HTTP_X_FORWARDED_FOR"),
            "PATH_INFO": request.META.get("PATH_INFO"),
            "REMOTE_ADDR": request.META.get("REMOTE_ADDR"),
        }
        payload = {
            "domain_id": settings.BASIC_ANALYTICS_ID,
            "request_meta": request_meta,
            "url": request.build_absolute_uri(),
        }
        requests.post(settings.BASIC_ANALYTICS_URL, json=payload)
        return super().dispatch(request, *args, **kwargs)
