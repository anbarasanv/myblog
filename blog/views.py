from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Post,Comment
from django.http import HttpResponse
from .forms import CommentForm

# Create your views here.
def post_list(request):

	posts = Post.objects.order_by('published_date')
	return render(request, 'blog/post_list.html',{'posts':posts})


class Detail(TemplateView):

	def post_details(request,slug):
		single_post = Post.objects.get(slug=slug)
		if request.method == 'GET':
			form = CommentForm()
			return render(request, 'blog/blog_detail.html',{'single_post':single_post, 'form': form})

		elif request.method == 'POST':
			form = CommentForm(request.POST)
			if form.is_valid():
				comment = form.save(commit = False)
				comment.post = single_post
				comment.user = request.user
				comment.save()
				form = CommentForm()
				comments = Comment.objects.order_by('time')
				context = {'single_post':single_post,
							'form': form,
							'comments':comments}
			return render(request, 'blog/blog_detail.html',context)

		else:
			form = CommentForm()
		return render(request, 'blog/blog_detail.html',{'single_post':single_post,'form': form})





def post_archive(request):
		form = CommentForm()
		posts = Post.objects.order_by('published_date')
		return render(request, 'blog/archive.html',{'posts':posts})






































