from django.utils import timezone
from geoip2.database import Reader
import geoip2.errors
from django.conf import settings
from .models import Visitor

class VisitorTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.city_reader = Reader(settings.GEOIP_CITY_PATH)
        self.country_reader = Reader(settings.GEOIP_COUNTRY_PATH)

    def __call__(self, request):
        ip_address = self.get_client_ip(request)
        if ip_address:
            city, country = self.get_location(ip_address)
            languages = ', '.join(request.META.get('HTTP_ACCEPT_LANGUAGE', '').split(','))
            Visitor.objects.create(
                ip_address=ip_address,
                country=country,
                city=city,
                languages=languages,
                visit_time=timezone.now()
            )
        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def get_location(self, ip_address):
        city = 'Unknown'
        country = 'Unknown'

        try:
            city_response = self.city_reader.city(ip_address)
            city = city_response.city.name or 'Unknown'
            country = city_response.country.name or 'Unknown'
        except geoip2.errors.AddressNotFoundError:
            try:
                country_response = self.country_reader.country(ip_address)
                country = country_response.name or 'Unknown'
            except geoip2.errors.AddressNotFoundError:
                pass

        return city, country
