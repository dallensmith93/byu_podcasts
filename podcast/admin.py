from django.contrib import admin
from .models import Podcast, Episode, Article, AboutUs

admin.site.register(Podcast)
admin.site.register(Episode)
admin.site.register(Article)
admin.site.register(AboutUs)

admin.site.site_header = "The Brigham Bros Podcast Admin"
admin.site.site_title = "The Brigham Bros Admin Portal"
admin.site.index_title = "Welcome to The Brigham Bros Podcast Admin"