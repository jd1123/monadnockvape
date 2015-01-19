from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from inventory.models import Category, SubCategory, InvItem
from django.core.urlresolvers import reverse
# Create your views here.
from monadnockvape.settings import DEBUG

# Create your views here.

@login_required
def index(request):
	context = RequestContext(request)
	context_dict = {}
	if request.method == 'GET':
		return render_to_response('juiceprogram/index.html', context, context_dict)
	elif request.method == 'POST':
		# look at post data and create a new user
		# but check if the user is already created
		
		return render_to_response('juiceprogram/index.html', context, context_dict)
	else:
		return Http404

@login_required
def user_lookup(request):
	if request.method == 'GET':
		context = RequestContext()
		context_dict = {}
		return render_to_response('juiceprogram/index.html', context, context_dict)
	elif request.method == 'POST':
		# allow changes to user juices etc
		
		return render_to_response('juiceprogram/index.html', context, context_dict)
	else:
		return Http404
