from django.shortcuts import render, redirect
from blog.models import Post
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from myblog.forms import SignupForm
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
	count = User.objects.count()
	posts = Post.objects.order_by('published_date')
	return render(request, 'myblog/home.html',{'posts':posts, 'count':count})

def signup(request):

	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username = username, password = raw_password)
			login(request, user)
			return redirect('home')
	else:
		form = SignupForm()
	return render(request,'myblog/signup.html',{'form':form})

@login_required
def secret_page(request):
	return render(request, 'myblog/secret_page.html')

def upload(request):
	context = {}
	if request.method == 'POST':
		uploaded_file = request.FILES['document']
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name, uploaded_file, max_length=None)
		context['url'] = fs.url(name)


	return render(request,'myblog/upload.html',context)
































# class SecretPage(LoginRequiredMixin,TemplateView):
# 	template_name = 'myblog/secret_page.html'
