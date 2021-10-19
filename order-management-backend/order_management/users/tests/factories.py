from django.contrib.auth.models import User


def create_user(**kwargs):
    password = kwargs.pop("password", "test")
    username = kwargs.pop("username", "test")
    user = User.objects.create_user(username=username, **kwargs)
    user.set_password(password)
    user.save()
    return user
