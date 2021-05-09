"""ipl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from stats import views as views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('update/',views.createprofile, name='update'),
    path('matchups/',views.matchuprecords, name='matchup'),
    path('m/',views.m, name='m'),
     path('matchup1/',views.matchup1, name='matchup1'),
    path('',views.home, name='home'),
    path('filterruns/',views.filterruns, name='filterruns'),
    path('filter/',views.filter, name='filter'),
    path('Fantasy',views.Fantasy , name= 'Fantasy'),
    path('PlayerStats', views.PlayerStats, name='PlayerStats'),
    path('About', views.About, name='About'),
    path('Contact', views.Contact, name='Contact'),
    path('Disclaimer', views.Disclaimer, name='Disclaimer'),
    path('teamlist/<str:id>', views.teamlist, name='teamlist'),
    path('cl/<str:id>', views.citylist, name='cl'),
    path('al/<str:id>', views.againstlist, name='al'),
    path('pl/<str:id>', views.positionlist, name='pl'),
   
    path('playerProfile/<str:id>', views.playerProfile, name='playerProfile'),
    path('playerProfile1/<int:id>', views.playerProfile1, name='playerProfile1'),
    path('playerProfile2/<int:id>', views.playerProfile2, name='playerProfile2'),
    path('playerProfile3/<int:id>', views.playerProfile3, name='playerProfile3'),
    path('playerProfile4/<int:id>', views.playerProfile4, name='playerProfile4'),
    path('playerProfile5/<str:id>', views.playerProfile5, name='playerProfile5'),
    path('playerProfile6/<str:id>', views.playerProfile5, name='playerProfile6'),
    path('playerProfile7/<str:id>', views.playerProfile5, name='playerProfile7'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('register', views.register, name='register'),
    path('search_player', views.search_players, name='search_player'),
    #path('ppupdate/', views.ppprofile, name='ppupdate')
]