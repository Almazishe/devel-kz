from django.conf import settings

from rest_framework import serializers, exceptions

from dj_rest_auth.serializers import LoginSerializer


class CustomLoginSerializer(LoginSerializer):
    """ Custom serializer is called when user is logging in.
    Created to handle auth not only by username but also 
    email and phone number
    """

    phone = serializers.CharField(required=False, allow_blank=True)

    def get_auth_user(self, username, email, phone, password):
        if email or username or phone and password:
            user = self.authenticate(username=username, email=email, password=password, phone=phone)
        else:
            msg = 'Must include either "username", "email" or "phone" and "password".'
            raise exceptions.ValidationError(msg)

        return user

    def validate(self, attrs):
        """ Authenticates and validates if user is active. Can
        also validate if email is verified but for now this 
        feature is not implemented.
        """

        username = attrs.get('username')
        email = attrs.get('email')
        phone = attrs.get('phone')
        password = attrs.get('password')
        user = self.get_auth_user(username, email, phone, password)

        if not user:
            msg = 'Unable to log in with provided credentials.'
            raise exceptions.ValidationError(msg)

        # Is User is active?
        self.validate_auth_user_status(user)

        # If required, is the email verified?
        # Will be required in future so leave it here.
        if 'dj_rest_auth.registration' in settings.INSTALLED_APPS:
            self.validate_email_verification_status(user)

        attrs['user'] = user
        return attrs