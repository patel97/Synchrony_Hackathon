"""Synchrony_Gamification URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.dashboard),
    url(r'^profile/', views.profile),
    url(r'^trading/', views.trading),
    url(r'^bet/', views.bet),
    url(r'^create_trade/', views.create_trade),
    url(r'^logout_complete/', views.logout_complete),
    url(r'^betting_status/', views.bettingstatus),
    url(r'^trade_creds/', views.trade_creds),
    url(r'^team_view/', views.team_view),
    url(r'^complete_call/', views.complete_call),
    url(r'^callfinal/', views.callfinal),



    url(r'^call/', views.call),


]
