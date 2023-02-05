from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

UserModel = get_user_model()


class TransporterCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('first_name', 'last_name', 'username')
        field_classes = {
            'username': auth_forms.UsernameField,
        }


class TransporterLogInForm(AuthenticationForm):
    pass