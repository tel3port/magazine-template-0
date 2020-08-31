from django.urls import path

from blog.views import HomeView
from . import views
from .feeds import LatestPostsFeed,AtomSiteNewsFeed


# urlpatterns = [
#     path('', HomeView.as_view(), name="blog-home"),
#     path('entry/<int:pk>/', EntryView.as_view(), name="entry-detail"),
#     path('create_entry/', CreateEntryView.as_view(success_url='/'), name='create_entry'),
#
# ]

urlpatterns = [
    # path('create_entry/', CreateEntryView.as_view(success_url='/'), name='create_entry'),
    # path('', views.home, name="blog-home"),
    path('', HomeView.as_view(), name="blog-home"),
    path('blog/<slug:slug>/', views.single_post, name="entry-detail"),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),

]
