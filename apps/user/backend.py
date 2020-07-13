from apps.user.models import User
from django.contrib.auth import backends


''' 
    No es necesario usarlo para el inicio de sesion con DRF y SimpleJwt
    debido a que si se usa no se puede obtener el token de acceso para iniciar sesion
'''


class EmailAuthBackend(backends.ModelBackend):
    """
    Email Authentication Backend

    Allows a other to sign in using an email/password pair, then check
    a username/password pair if email failed
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        """ Authenticate a other based on email address as the other name. """
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """ Get a User object from the user_id. """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
