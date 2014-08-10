# from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# Create your views here.


# Home page
def root(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('index.html', context_dict, context)


def about(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('about.html', context_dict, context)


def contact(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('contact.html', context_dict, context)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
