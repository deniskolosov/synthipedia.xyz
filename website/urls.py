from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'review-list/$', views.ReviewsView.as_view(), name = 'reviews'),
        url(r'^review/(?P<slug>[a-zA-Z-:0-9]+)$', views.ReviewView.as_view(), name='review'),
        url(r'^synths/(?P<slug>[a-zA-Z-:0-9/]+)$', views.SynthView.as_view(), name='synth'),
        url(r'synths-list/$', views.SynthsView.as_view(), name = 'synths'),
        url(r'add-synth$', views.SynthCreate.as_view(), name = 'add_synth'),
        ]
