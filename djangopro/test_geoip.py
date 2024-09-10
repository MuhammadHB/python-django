import geoip2.database

db_path = 'C:/Users/M/Downloads/GeoLite2-City_20240823/GeoLite2-City_20240823/GeoLite2-City.mmdb'

def test_geoip(ip_address):
    try:
        with geoip2.database.Reader(db_path) as reader:
            response = reader.city(ip_address)
            print("City:", response.city.name)
            print("Country:", response.country.name)
    except Exception as e:
        print("Error:", e)

test_geoip('182.52.87.80')  # استخدم عنوان IP معروف للتجربة
