from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from inventory.models import Category, SubCategory, InvItem
from django.core.urlresolvers import reverse
# Create your views here.


def root(request):
    return HttpResponse("Inventory Page")


def category_list(request):
    context = RequestContext(request)
    context_dict = {}
    c = Category.objects.all()
    context_dict['categories'] = c
    return render_to_response('inventory/category.html', context_dict, context)


def sub_category_list(request, category=None):
    context = RequestContext(request)
    context_dict = {}
    if category is None:
        return HttpResponseRedirect(reverse('inventory.category_list'))
    else:
        c = Category.objects.filter(category_name=decode_category(category))
        subs = SubCategory.objects.filter(category = c)
        print "Category : " + category
        if len(c) is 0:
            print "You are in the subcat list view"
            raise Http404
            #return HttpResponse("404 Not Found!")

        context_dict['subs'] = subs
        context_dict['category'] = c
        return render_to_response('inventory/sub_categories.html', context_dict, context)

def inv_item_list(request, category=None, sub_category = None):
    context = RequestContext(request)
    context_dict = {}
    print "Category: " + category
    print "Sub: " + sub_category


    if sub_category is None:
        return HttpResponseRedirect(reverse('inventory.sub_category_list'))
    else:
        c=Category.objects.filter(category_name=decode_category(category))
        s=SubCategory.objects.filter(sub_category_name=decode_category(sub_category))
        items=InvItem.objects.filter(category=c, sub_category=s)
        if len(items) is 0:
            raise Http404
        else:
            return render_to_response('inventory/inventory_items.html', context_dict, context)


def encode_category(category):
    s = category.split(' ')
    return '_'.join(s)

def decode_category(category):
    s = category.split('_')
    return ' '.join(s)
