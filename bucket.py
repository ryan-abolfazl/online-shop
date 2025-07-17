import boto3
from django.conf import settings


class Bucket:
    """CDN Bucket Manager

    init method creates connection.

    """
    def __init__(self):
        session = boto3.session.Session()
        self.client = session.client(
            service_name=settings.AWS_SERVICE,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            endpoint_url=settings.AWS_ENDPOINT_URL,

            )