import os
import django
from django.conf import settings
from django.contrib.gis.geoip2 import GeoIP2

# إعداد متغير البيئة لتحديد إعدادات Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangopro.settings')
django.setup()

def test_geoip(ip_address):
    try:
        g = GeoIP2()
        location = g.city(ip_address)
        print(location)
    except Exception as e:
        print("Error:", e)

# استبدل '8.8.8.8' بعنوان IP معروف
test_geoip('8.8.8.8')
