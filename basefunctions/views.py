# from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from basefunctions.models import IndexMosiac, IndexImage
from django.views.decorators.vary import vary_on_headers
# Create your views here.


# Home page
@vary_on_headers('User-Agent')
def root(request):
	context = RequestContext(request)
	context_dict = {}
	'''
        if request.method == 'POST':
		from_address = request.POST['email']
		name = request.POST['name']
		message = request.POST['message']
		message = "From: " + name + " " + email + "\n" + message
		send_mail('Contact Request', message, from_address, ['monadnockvapor@gmail.com'])
		return render_to_response('index2.html', context_dict, context)
	else:
        '''
	index_mosiac = IndexMosiac.objects.all()[0]
	field_names = sorted(index_mosiac._meta.get_all_field_names())
	images = []
	for f in field_names:
		if f.find('id') == -1 & f.find('name')==-1:
			print f, getattr(index_mosiac, f).image
			images.append((getattr(index_mosiac, f).image, getattr(index_mosiac, f).caption))

	context_dict['images'] = images
	return render_to_response('index2.html', context_dict, context)

def mosiac(request):
	context = RequestContext(request)
	context_dict = {}
	index_mosiac = IndexMosiac.objects.all()[0]
	field_names = index_mosiac._meta.get_all_field_names()
	images = []
	for f in field_names:
		if f.find('id') == -1:
			images.append(getattr(index_mosiac, f).image)

	context_dict['images'] = images

	return render_to_response('mosiac.html', context_dict, context)

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


def user_login(request):
    context = RequestContext(request)
    context_dict = {}
    refer = request.META.get('HTTP_REFERER')
    refer = '/' + '/'.join(str(refer).split('/')[3:])
    if request.GET:
        nxt = request.GET['next']
    else:
        nxt=refer

    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        if request.POST['next']:
            nxt = request.POST['next']
            print "assigned" + str(nxt)
        else:
            nxt = refer
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                print "Next: ",
                print nxt
                if nxt == 'None':
                    return HttpResponseRedirect('/juiceprogram/')
                else:
                    return HttpResponseRedirect('/juiceprogram/')
            else:
                return HttpResponse("Your account is disabled")
        else:
            print "Invalid login details {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details.")
    else:
        print "GET REQUEST: CHECK IF LOGGED IN"
        print request.user.is_authenticated()
        if request.user.is_authenticated():
            context_dict['auth'] = True
        context_dict['next'] = nxt
        return render_to_response('login.html', context_dict, context)


def user_logout(request):
    context = RequestContext(request)
    refer = request.META.get('HTTP_REFERER')
    refer = '/'+'/'.join(str(refer).split('/')[3:])

    if request.user.is_authenticated():
        logout(request)
        if refer:
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        return render_to_response('logout_error.html', context)
