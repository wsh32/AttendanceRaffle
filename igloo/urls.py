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
from django.contrib import admin as webmaster
from igloo import views
from api import account, auth, submit, adminsite
from api.config import config

handler500 = views.handler500
handler404 = views.handler404
handler403 = views.handler403
handler400 = views.handler400

urlpatterns = [
    url(r'^webmaster/', webmaster.site.urls),

    # Front End
    url(r'^$', views.home),
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^account/$', views.account),
    url(r'^submit/$', views.submit),

    # Back End
    url(r'^api/login/$', auth.login),
    url(r'^api/logout/$', auth.logout),
    url(r'^api/register/$', account.create_account),
    url(r'^api/submit/$', submit.submit),

    # Admin
    url(r'^admin/$', views.admin.home),
    url(r'^admin/raffle/$', views.admin.raffle),
    url(r'^admin/event/$', views.admin.event),

    url(r'^api/admin/login/$', adminsite.auth.login),
    url(r'^api/admin/logout/$', adminsite.auth.logout),
    url(r'^api/admin/draw/$', adminsite.raffle.draw),
    url(r'^api/admin/event/$', adminsite.event_management.add_event),
]

if config.ADMIN_CREATE:
    urlpatterns.append(url(r'^admin/register/$', views.admin.register))
    urlpatterns.append(url(r'^api/admin/register/$', adminsite.account.create_account))
