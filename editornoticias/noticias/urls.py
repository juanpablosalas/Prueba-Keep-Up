#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 16:26:32 2022

@author: juanpablosalas
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add, name='add'),
    #path('', views.VistaNoticias.as_view(), name='home'),
    #path('noticia/<int:pk>', views.VistaNoticiaDetallada.as_view(), name='detail'),
    path('noticia/<int:pk>/', views.detail, name='detail'),
    path('noticia/<int:pk>/edit', views.edit, name='edit'),
]