from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello World")

def current_datetime(request):
    now = datetime.datetime.now()
    #com a variavel TE#MPLATE_DIRS setada em settings.py e so dar um get_template para carregar o html na variavel t
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    # uma opcao encurtada e usar o shortcut render, daseguinte forma:
    #return render(request,'current_datetime.html',{'current_date':now})
    return HttpResponse(html)

def hours_ahead(request,offset):
    try:
        offset = int (offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
