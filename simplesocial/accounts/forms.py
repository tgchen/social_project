from django contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):

    class Meta:
        field = ('username','email','password1','password2')
        model = get_user_model()

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.field['username'].label='Display Name'
            self.field['email'].label='Email Address'
