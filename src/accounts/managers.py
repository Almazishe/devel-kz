from django.contrib.auth.models import UserManager


class CustomManager(UserManager):
    """ Custom manager for correctly handling 
    user and superuser creation.
    """
    
    def create_user(self, username, password, **other_params):

        if not other_params.get('email') and not other_params.get('phone_number'):
            raise ValueError('Email or Phone number must be set')
        
        user = self.model(username=username, **other_params)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **other_params):

        other_params.setdefault('is_staff', True)
        other_params.setdefault('is_superuser', True)
        other_params.setdefault('is_active', True)

        if other_params.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if other_params.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(password, username, **other_params)

