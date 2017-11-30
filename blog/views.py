from django.shortcuts import render
from django.template import loader

def post_list(request):
    return render(request, 'blog/post_list.html', {})
