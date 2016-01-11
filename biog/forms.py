# -*- coding: utf-8 -*-
"""

@author: idwaker
"""

from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'fullname', 'about',
        ]

