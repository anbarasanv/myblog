from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
	# post = forms.CharField()
	
	class Meta(object):
		"""docstring for Meta"""
		model = Comment
		fields = ('comment',)
		
			