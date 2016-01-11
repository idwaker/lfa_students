from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    fullname = models.CharField(max_length=255)
    address = models.TextField()
    key_skills = models.TextField()
    additional_skills = models.TextField()
    about = models.TextField()
    phone = models.CharField(max_length=16)
    linkedin_profile = models.TextField()
    github_projects = models.TextField()
    slideshare_links = models.TextField()
    youtube_links = models.TextField()
    additional_details = models.TextField()
    picture = models.ImageField(upload_to='uploads/')

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
