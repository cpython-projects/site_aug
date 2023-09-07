from django.db import models
from ckeditor.fields import RichTextField

class Footer(models.Model):
    address = RichTextField()
    reservation = RichTextField()
    opening_hours = RichTextField()
    twitter_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    copyright_text = RichTextField()
    credits_text = RichTextField()

    def __str__(self):
        return 'Footer Info'