# myapp/utils.py
import facebook
import logging
from django.conf import settings

# Set up logging
logger = logging.getLogger(__name__)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def post_facebook_comment(post_id, message):
    try:
        graph = facebook.GraphAPI(access_token=settings.FACEBOOK_APP_TOKEN)
        graph.put_object(parent_object=post_id, connection_name='comments', message=message)
        logger.info(f"Successfully posted comment to post {post_id}")
        return True
    except facebook.GraphAPIError as e:
        logger.error(f"Error posting comment: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return False
