from django.shortcuts import render
from django.http import HttpResponse

from .models import Review


def index(request):
    review_list = Review.objects.order_by('-pub_date')
    context = {
        'review_list': review_list,
    }

    return render(request, 'comments_page/index.html', context)
