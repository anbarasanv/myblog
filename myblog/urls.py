"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path

# To Add Static and Media Files path 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

# To add views url
from . import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home),
	url(r'^home/$',views.home, name= 'home'),
    url(r'signup/$',views.signup, name = 'signup'),
    url(r'^blog/',include('blog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('secret/', views.secret_page, name= 'secret'),
    url(r'^upload/$', views.upload, name='upload'),
    # path('secret2/', views.SecretPage.as_view(), name= 'secret2')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
