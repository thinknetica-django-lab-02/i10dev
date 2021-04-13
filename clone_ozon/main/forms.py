from django.forms import inlineformset_factory, ModelForm
from django.contrib.auth.models import User
from .models import Profile


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('name',)
