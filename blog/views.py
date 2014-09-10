from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from blog.Models import BlogPost
from django.contrib.auth.decorators import login_requires
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    context = RequestContext(request)
    context_dict = {}

    allposts = BlogPost.objects.all().order_by("-created")
    p = Paginator(allposts, 5)
    try:
        recent_posts = p.page(1).object_list
    except:
        recent_posts = p.page(1).object_list

    posts = []

    for i in recent_posts:
        words = i.body.split(' ')
        if len(words) < 30:
            l = len(words)
        else:
            l=30

        slug = ' '.join([x for x in words[0:l]]) + "..."
        posts.append({'title':i.title,
                      'slug': slug,
                      'pk': i.pk,
                      'object':i})

    context_dict['posts'] = posts
    return render_to_response('blog/index.html', context_dict, context)
