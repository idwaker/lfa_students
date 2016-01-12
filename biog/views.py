# -*- coding: utf-8 -*-
"""
"""
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout

from .models import User
from .forms import ProfileForm, LoginForm


def home(request):
    pass


def userlogin(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/profile/' + username)
            else:
                messages.warning(request, "This account is not active",
                                 extra_tags='warning')
        else:
            messages.error(request, "Invalid Username or Password",
                           extra_tags='alert')
    return render(request, 'login.html', dict(form=form))


def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/login')


def profile(request, username):
    user = get_object_or_404(User, username=username.strip())
    if not user.userprofile:
        raise Http404("Page Not Found")

    form = ProfileForm(request.POST or None, request.FILES or None,
                       instance=user.userprofile)
    if form.is_valid():
        # if request.POST.get('user_id') != request.user.id:
        #    messages.error(request, "Unauthorized Access", extra_tags='alert')
        #    return HttpResponseRedirect('/profile/' + username)
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Profile updated Successfully",
                         extra_tags="done")

    return render(request, 'profile.html', {'userprofile': user.userprofile,
                                            'form': form})

