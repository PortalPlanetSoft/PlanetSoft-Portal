from django.contrib.auth.forms import UserCreationForm
from users.models import User


class CustomCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
