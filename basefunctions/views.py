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
	
        index_mosiac = IndexMosiac.objects.all()[0]
	field_names = sorted(index_mosiac._meta.get_all_field_names())
	imgobj = []
	for f in field_names:
		if f.find('id') == -1 & f.find('name')==-1:
			imgobj.append(getattr(index_mosiac, f))
	
	for i in range(len(imgobj)):
		imgobj[i].num = i + 1
                if (i+1)%3 == 0:
			imgobj[i].br = True


	context_dict['imgobj'] = imgobj
	return render_to_response('index.html', context_dict, context)

# not a view
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
