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
        widgets = {
            'address': forms.TextArea(attrs={'rows': 2, 'cols': 40}),
            'key_skills': forms.TextArea(attrs={'rows': 2, 'cols': 40}),
            'additional_skills': forms.TextArea(attrs={'rows': 2, 'cols': 40}),
            'about': forms.TextArea(attrs={'rows': 2, 'cols': 40}),
            'linkedin_profile': forms.TextArea(attrs={'rows': 1, 'cols': 40}),
            'github_projects': forms.TextArea(attrs={'rows': 3, 'cols': 40}),
            'slideshare_links': forms.TextArea(attrs={'rows': 3, 'cols': 40}),
            'youtube_links': forms.TextArea(attrs={'rows': 3, 'cols': 40}),
            'additional_details': forms.TextArea(attrs={'rows': 3, 'cols': 40}),
        }

