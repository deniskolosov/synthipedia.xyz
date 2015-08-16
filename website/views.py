from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from .models import Synth, Review
from .forms import SynthForm

class ReviewsView(generic.ListView):
    template_name = 'website/reviews.html'
    context_object_name = 'latest_review_list'
    model = Review

    def get_context_data(self, **kwargs):
        context = super(ReviewsView, self).get_context_data(**kwargs)
        latest_review_list = Review.objects.order_by('-synth')[:5]
        context['pagetab'] = 'reviews'
        context['latest_review_list'] = latest_review_list
        return context


class ReviewView(generic.DetailView):
    model = Review
    template_name = 'website/review.html'

    def get_context_data(self, **kwargs):
        context = super(ReviewView, self).get_context_data(**kwargs)
        context['pagetab'] = 'reviews'
        return context

class SynthView(generic.DetailView):
    model = Synth
    template_name = 'website/synth.html'

    def get_context_data(self, **kwargs):
        context = super(SynthView, self).get_context_data(**kwargs)
        context['pagetab'] = 'synths'
        return context

class SynthsView(generic.ListView):
    model = Synth
    template_name = 'website/synths.html'
    context_object_name = 'synths'

    def get_context_data(self, **kwargs):
        #Call the base implementation first to get a context
        synths_list = Synth.objects.all()
        synth_reviews = [s.review_set.all() for s in synths_list]
        context = super(SynthsView, self).get_context_data(**kwargs)
        context['pagetab']='synths'
        context['synths_list']=synths_list
        context['synth_reviews']=synth_reviews
        return context

class SynthCreate(CreateView):
    model = Synth
    template_name='website/add_synth.html'
    success_url = reverse_lazy('synths')
    fields = ['name','issue_year','category','pic','maker']
