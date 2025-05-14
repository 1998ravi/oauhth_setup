import jwt
import datetime
import uuid

from django.conf import settings
from oauth2_provider.oauth2_validators import OAuth2Validator
from django.utils import timezone

class CustomOAuth2Validator(OAuth2Validator):
    def save_bearer_token(self, token, request, *args, **kwargs):
        access_expires = timezone.now() + datetime.timedelta(
            seconds=settings.OAUTH2_PROVIDER["ACCESS_TOKEN_EXPIRE_SECONDS"]
        )
        refresh_expires = timezone.now() + datetime.timedelta(
            seconds=settings.OAUTH2_PROVIDER["REFRESH_TOKEN_EXPIRE_SECONDS"]
        )

        access_payload = {
            "jti": str(uuid.uuid4()),
            "exp": int(access_expires.timestamp()),
            "iat": int(timezone.now().timestamp()),
            "token_type": "access",
            "client_id": request.client.client_id,
            "scope": token["scope"],
        }

        refresh_payload = {
            "jti": str(uuid.uuid4()),
            "exp": int(refresh_expires.timestamp()),
            "iat": int(timezone.now().timestamp()),
            "token_type": "refresh",
            "client_id": request.client.client_id,
            "scope": token["scope"],
        }

        if request.user and hasattr(request.user, "id"):
            # If the request is associated with a user
            access_payload["user_id"] = request.user.id
            refresh_payload["user_id"] = request.user.id
        else:
            # If there is no authenticated user (e.g. client credentials flow)
            access_payload["user_id"] = None
            refresh_payload["user_id"] = None

        token["access_token"] = jwt.encode(
            access_payload,
            settings.PRIVATE_KEY,
            algorithm="RS256"
        ).decode("utf-8")


        super().save_bearer_token(token, request, *args, **kwargs)
