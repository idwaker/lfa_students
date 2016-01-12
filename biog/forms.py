# -*- coding: utf-8 -*-
"""

@author: idwaker
"""

from django import forms
from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=64)
    password = forms.CharField(label='Password', max_length=250,
                               widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['fullname', 'address', 'key_skills', 'additional_skills',
                  'about', 'linkedin_profile', 'github_projects',
                  'slideshare_links', 'youtube_links', 'additional_details',
                  'picture']

