from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from inventory.models import Category, SubCategory, InvItem
# Create your views here.


def root(request):
    return HttpResponse("Inventory Page")


def category_page(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('inventory/category.html', context_dict, context)


def sub_category_page(request, category=None):
    context = RequestContext(request)
    context_dict = {}
    if category is None:
        return HttpResponseRedirect(reverse('siteroot.category_page'))
    else:
        return HttpResponse("You are looking at sub_categories")
