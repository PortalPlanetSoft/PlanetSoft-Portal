from django.contrib.auth.signals import user_logged_in, user_login_failed, user_logged_out
from django.dispatch import receiver

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    print('user logged in {} logged in trought page {}'.format(user.username, request.META.get('HTTP_REFER')))

@receiver(user_login_failed)
def log_user_login_field(sender, credntials, request, **kwargs):
    print('user field to log in {} field to login in trought page {}'.format(user.username, request.META.get('HTTP_REFER')))

@receiver(user_logged_out)
def  log_user_logout(sender, request, user, **kwargs):
    print('user logged out {} logged out trought page {}'.format(user.username, request.META.get('HTTP_REFER')))


