from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.utils.translation import ugettext as _
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.db import models
from django.contrib.auth.models import User, SiteProfileNotAvailable
from django.template import RequestContext
from django.conf import settings
from map.forms import *
from xml.dom import minidom
import urllib2
import random
import cPickle as pickle
import base64
import Image
import urllib
import os
from googlemaps import GoogleMaps
import yql

GOOGLE_MAPS_API_KEY = hasattr(settings, "GOOGLE_MAPS_API_KEY") and \
                      settings.GOOGLE_MAPS_API_KEY or None

def fetch_geodata(request, lat, lng):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        url = "http://ws.geonames.org/countrySubdivision?lat=%s&lng=%s" % (lat, lng)
        dom = minidom.parse(urllib.urlopen(url))
        country = dom.getElementsByTagName('countryCode')
        if len(country) >=1:
            country = country[0].childNodes[0].data
        region = dom.getElementsByTagName('adminName1')
        if len(region) >=1:
            region = region[0].childNodes[0].data

        return HttpResponse(simplejson.dumps({'success': True, 'country': country, 'region': region}))
    else:
        raise Http404()


def parse(dest):
    addr=dest.split(',')
    alen = len(addr)
    print addr
    if len(addr) > 3:
        return addr[1]+","+addr[2]+","+addr[3]
    return addr[1]+","+addr[2]


def index(request):
    """
    Main Page
    """
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            
            gmaps = GoogleMaps(GOOGLE_MAPS_API_KEY)
            destination = gmaps.latlng_to_address(form.cleaned_data.get('latitude'), form.cleaned_data.get('longitude'))
            print destination
            destination=parse(destination)
            print destination                        
            y=yql.Public()
            query='select * from google.news where q="'+destination+'"'
            print query
            res=y.execute(query,env='store://datatables.org/alltableswithkeys')
            rows = res.rows
    else:
        form = LocationForm()
        rows = {}

    template = "map/index.html"
    data = { 'GOOGLE_MAPS_API_KEY': GOOGLE_MAPS_API_KEY,
             'form': form, 'res':rows }
    return render_to_response(template, data, context_instance=RequestContext(request))

