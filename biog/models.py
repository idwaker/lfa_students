# -*- coding: utf-8 -*-
"""

"""

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    fullname = models.CharField(max_length=255)
    address = models.TextField(blank=True, default='')
    key_skills = models.TextField(blank=True, default='')
    additional_skills = models.TextField(blank=True, default='')
    about = models.TextField(blank=True, default='')
    phone = models.CharField(max_length=16, blank=True, default='')
    linkedin_profile = models.TextField(blank=True, default='')
    github_projects = models.TextField(blank=True, default='')
    slideshare_links = models.TextField(blank=True, default='')
    youtube_links = models.TextField(blank=True, default='')
    additional_details = models.TextField(blank=True, default='')
    picture = models.ImageField(upload_to='uploads/', blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname

    __unicode__ = __str__

    def key_skills_aslist(self):
        return self.key_skills.strip().split(",")

    def additional_skills_aslist(self):
        return self.additional_skills.strip().split(",")

    def github_projects_aslist(self):
        return [tuple(each.split('/')) for each in
                self.github_projects.strip().split()]

    def slideshare_links_aslist(self):
        return self.slideshare_links.strip().split()

    def youtube_links_aslist(self):
        return self.youtube_links.strip().split()

    @property
    def is_complete(self):
        # FIXME: Hack
        return self.fullname.strip() and self.address.strip() and \
                self.key_skills.strip() and self.additional_skills.strip() and \
                self.about.strip() and self.phone.strip() and \
                self.linkedin_profile.strip() and self.github_projects.strip() and \
                self.slideshare_links.strip() and self.youtube_links.strip() and \
                self.additional_details.strip() and self.user.email

