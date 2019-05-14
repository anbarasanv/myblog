from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
	"""docstring for ClassName"""
	first_name = forms.CharField(max_length=40, required =False, help_text='optional.')
	last_name = forms.CharField(max_length=40, required =False, help_text='optional.')
	email = forms.EmailField(max_length=254, help_text='required, Please enter valid email address.')

	class Meta(object):
		"""docstring for Meta"""
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
			