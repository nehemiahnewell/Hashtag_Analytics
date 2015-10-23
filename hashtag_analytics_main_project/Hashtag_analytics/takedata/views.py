from django.shortcuts import render, loader, HttpResponse, RequestContext, get_object_or_404,get_list_or_404
from savedata.models import searchData, hashtags
#Create your views here.

def start_home_page(request):
    return render(request,"frontpage.html")

def start_arhive_page(request):
    hashsearch_list = searchData.objects.all()
    template = loader.get_template('records.html')
    records = RequestContext(request, {'hashsearch_list' : hashsearch_list})
    return HttpResponse(template.render(records))

def search(request, hashSearch_id):
    hashSearch = get_list_or_404(hashtags, search_id=hashSearch_id)
    hashSearch_list = get_object_or_404(searchData, id=hashSearch_id)
    return render(request, 'search.html', {'search':hashSearch,'record':hashSearch_list})