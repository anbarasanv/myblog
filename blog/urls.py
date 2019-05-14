from django.conf.urls import url 
from . import views


app_name = 'blog'

urlpatterns = [
	url(r'^$',views.post_list, name='list'),
	url(r'^posts/$',views.post_archive, name='posts'),
	url(r'^post/(?P<slug>[\w-]+)/$',views.Detail.post_details, name='detail'),
	
	
	

	
]
