"""igloo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from igloo import views
from api import account, auth, submit

handler500 = views.handler500
handler404 = views.handler404
handler403 = views.handler403
handler400 = views.handler400

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	
    url(r'^400/', views.handler400),
    url(r'^403/', views.handler403),
    url(r'^404/', views.handler404),
    url(r'^500/', views.handler500),

    # Front End
    url(r'^$', views.home),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^account/', views.account),
    url(r'^submit/', views.submit),

    # Back End
    url(r'^api/login/', auth.login),
    url(r'^api/logout/', auth.logout),
    url(r'^api/register/', account.create_account),
    url(r'^api/submit/', submit.submit),
]
