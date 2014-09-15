# from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from inventory.models import Category, SubCategory, InvItem
from django.core.urlresolvers import reverse
# Create your views here.
from monadnockvape.settings import DEBUG


def root(request):
    return HttpResponse("Inventory Page")


def category_list(request):
    context = RequestContext(request)
    context_dict = {}
    c = Category.objects.all()
    args = [(cat, encode_category(cat.category_name)) for cat in c]
    context_dict['categories'] = c
    context_dict['args'] = args
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
            raise Http404

        context_dict['subs'] = subs
        context_dict['category'] = (c[0].category_name, encode_category(c[0].category_name))
        args = [(s, encode_category(s.sub_category_name)) for s in subs]
        context_dict['args'] = args
        return render_to_response('inventory/sub_categories.html', context_dict, context)


def inv_item_list(request, category=None, sub_category = None):
    context = RequestContext(request)
    context_dict = {}

    if DEBUG is True:
        print "Category: " + category
        print "Sub: " + sub_category
        print str(sub_category == 'all')

    if sub_category is None:
        return HttpResponseRedirect(reverse('inventory.sub_category_list'))

    elif sub_category == 'all':
        try:
            c=Category.objects.filter(category_name=decode_category(category))
            context_dict['category'] = c[0].category_name
            context_dict['sub_category'] = 'all'
            context_dict['items'] = [(x,encode_category(x.item_name)) for x in InvItem.objects.filter(category=c)]
            context_dict['all'] = True
            return render_to_response('inventory/inventory_items.html', context_dict, context)

        except IndexError:
            raise Http404

    else:
        try:
            c = Category.objects.filter(category_name=decode_category(category))
            s = SubCategory.objects.filter(sub_category_name=decode_category(sub_category))
            context_dict['category'] = (c[0].category_name, encode_category(c[0].category_name))
            context_dict['sub_category'] = (s[0].sub_category_name, encode_category(s[0].sub_category_name))
            context_dict['items'] = [(x, encode_category(x.item_name)) for x in InvItem.objects.filter(category=c, sub_category=s)]
            return render_to_response('inventory/inventory_items.html', context_dict, context)

        except IndexError:
            raise Http404

def single_item_view(request, category, sub_category, item_stub):
    context = RequestContext(request)
    context_dict = {}
    item = decode_category(item_stub)
    inv_item = InvItem.objects.filter(item_name=item)[0]
    context_dict['item_name']=inv_item.item_name
    context_dict['price'] = inv_item.price
    context_dict['description'] = inv_item.description
    context_dict['pic_url'] = inv_item.picture_url
    print context_dict

    return render_to_response('inventory/single_item.html', context_dict, context)

def encode_category(category):
    s = category.split(' ')
    return '_'.join(s)


def decode_category(category):
    s = category.split('_')
    return ' '.join(s)
