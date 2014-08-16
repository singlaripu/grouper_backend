
from django.conf.urls import patterns, include, url

from .views import HomePageView




# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
    # Admin panel and documentation:
    url('^$', HomePageView.as_view(), name='home'),
)
