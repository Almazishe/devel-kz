from django.contrib.auth.backends import ModelBackend

from src.accounts.models import CustomUser


class CustomUserBackend(ModelBackend):
    """ Was created to handle authentication not only 
    with username but also email and phone number.
    The calling serializer is validating inputs so there 
    is 100% that one of 3 unique fields is not None.
    """
    
    def authenticate(self, request, username=None, email=None, phone=None, **kwargs):
        password = kwargs['password']

        try:
            if phone:
                user = CustomUser.objects.get(phone=phone)
            elif email:
                user = CustomUser.objects.get(email=email)
            elif username:
                user = CustomUser.objects.get(username=username)

            if user.check_password(password) is True:
                return user
        except CustomUser.DoesNotExist:
            return None

