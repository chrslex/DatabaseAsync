from django.shortcuts import render
from django.db.models import Q
from .models import Person
import re

def person_list(request):
    people = Person.objects.order_by('nim_tpb')
    return render(request, 'people.html', {'people' : people})

def sort(request):
    order = request.GET.get('order_by','')
    people = Person.objects.all().order_by(order)
    return render(request, 'people.html', {'people' : people})

def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query = request.GET['q']
        filterarr = ['nama', 'panggilan', 'jenis_kelamin']
        if (query.startswith('nim=') or query.startswith('n=')):
            filterarr.append('nim_tpb')
            filterarr.append('nim_jurusan')
            query = query.replace('nim=', '')
            query = query.replace('n=', '')
        if (query.startswith('jurusan=') or query.startswith('j=')):
            filterarr.append('jurusan')
            query = query.replace('jurusan=', '')
            query = query.replace('j=', '')
        if (query.startswith('kelompok=') or query.startswith('k=') or query.startswith('kel=')):
            filterarr.append('kelompok')
            query = query.replace('kelompok=', '')
            query = query.replace('k=', '')
            query = query.replace('kel=', '')
        entry_query = get_query(query, filterarr)
        found_entries = Person.objects.filter(entry_query)
    return render(request, 'people.html', {'people': found_entries})

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query
