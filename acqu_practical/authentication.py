from django.contrib.auth import authenticate
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from django.utils.translation import gettext as _
from practical.serializers import Usersserializer
from django.db.models import Q
from practical.models import User


def authenticate_user(self, request, username, password, is_owner=False):
    q_filt = Q()
    q_filt |= Q(email__iexact=username)
    q_filt |= Q(username__iexact=username)

    try:
        user_obj = authenticate(
            username=User.objects.filter(
                q_filt).first().username, password=password
        )
    except Exception as e:
        raise NotFound(_("The username or password is incorrect!"))

    if user_obj:
        user = Usersserializer(instance=user_obj)
        data = user.data
        return Response(data)
    else:
        raise NotFound(_("User does not exist"))
