from django.conf.urls import url, include
from django.urls import path
from django.views.generic.base import RedirectView
from .views import  (
	UserDetailView,
	UserFollowView
	)

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'),
    url(r'^(?P<username>[\w.@+-]+)/follow/$', UserFollowView.as_view(), name='follow'),
    # url(r'^$',RedirectView.as_view(url="/")),    
    # url(r'^search', TweetListView.as_view(), name='list'),
    # url(r'^create/$', TweetCreateView.as_view(), name='create'),
    # url(r'^(?P<pk>\d+)$', UserDetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'),
]
