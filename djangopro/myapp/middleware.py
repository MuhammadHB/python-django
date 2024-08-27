import geoip2.database
from django.utils.deprecation import MiddlewareMixin
from django.utils.translation import get_language
from django.utils import timezone
from myapp.models import Visitor
import logging

logger = logging.getLogger(__name__)

class VisitorTrackingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        ip_address = x_forwarded_for.split(',')[0].strip() if x_forwarded_for else request.META.get('REMOTE_ADDR')

        # Skip processing for local addresses
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
                    country_name = response.country.name
                    city_name = response.city.name
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
