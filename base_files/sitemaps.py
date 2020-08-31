from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from blog.models import Entry


class StaticViewsBlogSitemap(Sitemap):
    changefreq = 'always'
    priority = 1.0

    def items(self):
        return Entry.objects.all()

#     def location(self, item):
#         return reverse(item)


# class StaticViewsGallerySitemap(Sitemap):
#     def items(self):
#         return ['home']
#
#     def location(self, item):
#         return reverse(item)
