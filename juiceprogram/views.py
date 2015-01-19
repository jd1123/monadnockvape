from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from monadnockvape.settings import DEBUG
from juiceprogram.models import Customer, new_customer

# Create your views here.

@login_required
def index(request):
	context = RequestContext(request)
	context_dict = {}
	if request.method == 'GET':
		return render_to_response('juiceprogram/index.html', context_dict, context)
	elif request.method == 'POST':
                fname = request.POST['first_name']
                lname = request.POST['last_name']
                juices_purchased = request.POST['juices']
                juices_claimed = request.POST['claimed']
                ## Check if customer exists
                print "Checking customer"
                if len(Customer.objects.filter(first_name=fname, last_name=lname)) == 0:
                    print "creating customer"
                    c = new_customer(fname, lname, juices_purchased, juices_claimed)
                    context_dict["created"]=True
                    context_dict["customer"] = c
                    print context_dict
		return render_to_response('juiceprogram/index.html',context_dict,context)
	else:
		return Http404

@login_required
def user_view(request, id_num):
    context = RequestContext(request)
    context_dict = {}
    if request.method == "GET":
        cust = Customer.objects.filter(id_num = id_num)
        if cust == []:
            pass
            # do something
        else:
            pass
            # render it to the page
    elif request.method == "POST":
        pass
        #change the data
    else:
        return Http404



@login_required
def user_lookup(request):
	if request.method == 'GET':
		context = RequestContext()
		context_dict = {}
		return render_to_response('juiceprogram/index.html', context_dict, context)
	elif request.method == 'POST':
		# allow changes to user juices etc
		
		return render_to_response('juiceprogram/index.html', context_dict, context)
	else:
		return Http404
