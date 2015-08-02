from django.shortcuts import render

from .models import Synth, Review
# Create your views here.


def index(request):
    latest_review_list = Review.objects.order_by('-synth')[:5]
    context = {'latest_review_list' : latest_review_list}
    return render(request, 'website/index.html', context)

