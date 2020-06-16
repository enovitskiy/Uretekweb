from django.contrib.sitemaps import Sitemap
from .models import Navconstruct,Subnavigator, Example

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    protocol = 'https'
    def items(self):
        return Subnavigator.objects.exclude(subname=None)

class PostSitemap1(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    protocol = 'https'
    def items(self):
        return Navconstruct.objects.all()

class PostSitemap2(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    protocol = 'https'
    def items(self):
        return Example.objects.all()