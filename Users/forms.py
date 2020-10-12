from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError


def validate_username(value):
    for char in value:
        if not char.isnumeric() and not char.isalpha():
            raise ValidationError("Username should contains only letters and digits")

    if len(value) < 5:
        raise ValidationError("Username should have minimum 5 characters")
    else:
        return value


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators = [validate_username]

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email']
