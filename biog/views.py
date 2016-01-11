#! -*- coding: utf-8 -*-
"""
"""
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import User

# Create your views here.


def home(request):
    pass


def profile(request, username):
    user = get_object_or_404(User, username=username.strip())
    if not user.userprofile:
        raise Http404("Page Not Found")
    return render(request, 'profile.html', {'user': user.userprofile})
