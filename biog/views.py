# -*- coding: utf-8 -*-
"""
"""
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import User
from .forms import ProfileForm


def home(request):
    pass


def profile(request, username):
    user = get_object_or_404(User, username=username.strip())
    if not user.userprofile:
        raise Http404("Page Not Found")
    return render(request, 'profile.html', {'user': user.userprofile})


def update_profile(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Created", extra_tags="done")
    return render(request, 'profile.html', {'form': form})

