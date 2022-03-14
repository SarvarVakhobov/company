from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import Custom_user, Workers

class Com_userForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Custom_user
        fields = ['username', 'email', 'name', 'category_company']

class WorkersForm(ModelForm):
    class Meta(ModelForm):
        model = Workers
        fields = ['username', 'category_worker', 'password1', 'password2']

class Worker_editForm(ModelForm):
    class Meta(ModelForm):
        model = Workers
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'gender', 'email', 'number', 'avatar']

class Com_editForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = Custom_user
        fields = ['username','name', 'category_company', 'first_name', 'last_name', 'email', 'number', 'avatar', 'bio', 'telegram_link', 'instagram_link','facebook_link']
