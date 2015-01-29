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
		raise Http404

@login_required
def user_view(request, id_num):
    context = RequestContext(request)
    context_dict = {}
    if request.method == "GET":
        cust = Customer.objects.filter(id_num = id_num)
        if len(cust) == 0:
            # raise Http404
            context_dict['id_num'] = id_num
            return render_to_response("juiceprogram/user_view.html", context_dict, context)
        else:
            cust = cust[0]
            context_dict['customer'] = True
            context_dict['id_num'] = id_num
            context_dict['first_name'] = cust.first_name
            context_dict['last_name'] = cust.last_name
            context_dict['juices_purchased'] = cust.juices_purchased
            context_dict['juices_claimed'] = cust.juices_claimed
            context_dict['juices_eligible'] = (cust.juices_purchased % 5) - cust.juices_purchased - cust.juices_claimed
            print context_dict
            return render_to_response("juiceprogram/user_view.html", context_dict, context)
            # render it to the page
    elif request.method == "POST":
        cust = Customer.objects.filter(id_num = id_num)
        if len(cust) == 0:
            # raise Http404
            context_dict['id_num'] = id_num
            return render_to_response("juiceprogram/user_view.html", context_dict, context)
        else:
            cust = cust[0]
            context_dict['customer'] = True
            context_dict['id_num'] = id_num
            context_dict['first_name'] = cust.first_name
            context_dict['last_name'] = cust.last_name
            context_dict['juices_purchased'] = cust.juices_purchased
            context_dict['juices_claimed'] = cust.juices_claimed
            context_dict['juices_eligible'] = cust.juices_purchased/5 - (cust.juices_purchased % 5)/5 - cust.juices_claimed
            if request.POST.get("addjuice"):
                cust.juices_purchased = cust.juices_purchased + 1
                context_dict['juices_purchased'] = cust.juices_purchased 
                context_dict['juices_eligible'] = cust.juices_purchased/5 - (cust.juices_purchased % 5)/5 - cust.juices_claimed
                cust.save()
                return render_to_response("juiceprogram/user_view.html", context_dict, context)
            elif request.POST.get("claim"):
                cust.juices_claimed = cust.juices_claimed + 1
                context_dict['juices_purchased'] = cust.juices_purchased 
                context_dict['juices_eligible'] = cust.juices_purchased/5 - (cust.juices_purchased % 5)/5 - cust.juices_claimed
                cust.save()
                return render_to_response("juiceprogram/user_view.html", context_dict, context)
    else:
        raise Http404



@login_required
def user_lookup(request):
	context = RequestContext(request)
	context_dict = {}
	if request.method == 'GET':
		return render_to_response('juiceprogram/user_lookup.html', context_dict, context)
	elif request.method == 'POST':
		lname = request.POST['last_name']
		fname = request.POST['first_name']
		id_num = request.POST['id']
		if id_num != '':
			custs=Customer.objects.all().filter(id_num = id_num)
		elif lname != '':
			custs = Customer.objects.all().filter(last_name = lname)
			if fname != '':
				custs.filter(first_name = fname)
		elif fname != '':
			custs = Customer.objects.all().filter(first_name = fname)
		else:
			context_dict['error'] = "Nothing found!"
		
		if len(custs) != 0:
			context_dict['customers']=custs
		return render_to_response('juiceprogram/user_lookup.html', context_dict, context)
	else:
		raise Http404
