from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit


def home_page_view(request):   
    return about_page_view(request)


def about_page_view(request):

    queryset = PageVisit.objects.all()

    my_title = 'my page'
    content = 'dem titties'
    title_test = 'hi'

    PageVisit.objects.create()

    my_context = {
        'page_title': my_title,
        'page_content': content,
        'title_test' : title_test,
        'queryset' : queryset,
        'page_count' : queryset.count(),
    } 
    
    return render(request, 'home.html', my_context)