# myapp/middleware.py

import geoip2.database
from django.utils.deprecation import MiddlewareMixin
from django.utils.translation import get_language
from django.utils import timezone
from .models import Visitor
from .utils import get_client_ip
import logging

logger = logging.getLogger(__name__)

class VisitorTrackingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip_address = get_client_ip(request)
        
        if ip_address.startswith('127.0.0.1') or ip_address == '::1':
            country_name = "Local"
            city_name = "Local"
        else:
            country_name = "Unknown"
            city_name = "Unknown"
            
            try:
                db_path = 'C:/Users/M/Downloads/GeoLite2-City_20240823/GeoLite2-City_20240823/GeoLite2-City.mmdb'
                with geoip2.database.Reader(db_path) as reader:
                    response = reader.city(ip_address)
                    country_name = response.country.name or "Unknown"
                    city_name = response.city.name or "Unknown"
                    logger.info(f"IP: {ip_address} - Country: {country_name} - City: {city_name}")
            except geoip2.errors.AddressNotFoundError:
                logger.warning(f"Address {ip_address} not found in GeoIP database.")
            except Exception as e:
                logger.error("GeoIP lookup error:", exc_info=e)
        
        ui_languages = get_language() or "Unknown"

        Visitor.objects.create(
            ip_address=ip_address,
            country_name=country_name,
            city_name=city_name,
            ui_languages=ui_languages,
            visit_time=timezone.now()
        )
