"""Museum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from Museum01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^login', views.login),
    url(r'^register', views.register),
    url(r'^home', views.home),
    url(r'^first_qin', views.first_qin),
    url(r'^qing_han', views.qing_han),
    url(r'^sui_tang', views.sui_tang),
    url(r'^two_song', views.two_song),
    url(r'^y_m_q', views.y_m_q),
    url(r'^module', views.module),
    url(r'^single_module', views.single_module),
    url(r'^search', views.search),
    url(r'^single_cloth', views.single_cloth),
    url(r'^add_cloth', views.add_cloth),
]
