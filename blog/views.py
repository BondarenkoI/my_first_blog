from django.shortcuts import render
from django.utils import time_zone
from .models import Post

def post_list(request):
	posts = Post.objects.filter(published_date_lte=time_zone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {})


Post.objects.filter(published_date_lte=time_zone.now()).order_by('published_date')	