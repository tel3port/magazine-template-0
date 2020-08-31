from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Entry
from django.urls import reverse
from django.utils.feedgenerator import Atom1Feed


class LatestPostsFeed(Feed):
    title = "Cool blog"
    link = ""
    description = "New posts of my blog."

    def items(self):
        return Entry.objects.filter(status=1)

    def item_title(self, item):
        return item.entry_title

    def item_description(self, item):
        return truncatewords(item.entry_text, 50)


class AtomSiteNewsFeed(LatestPostsFeed):
    feed_type = Atom1Feed
    subtitle = LatestPostsFeed.description
