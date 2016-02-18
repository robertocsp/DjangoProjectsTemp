from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect
from books.models import Book
import datetime
from forms import ContactForm
from django.core.mail import send_mail

def hello(request):
    return HttpResponse(request.is_secure())

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

def itens_do_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k,v in values:
        html.append(('<tr><td>%s</td><td>%s</td></tr>' % (k, v)))
    html.append('Username: ' + request.user.username)
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search_form(request):
    return render(request,'search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render (request,'search_results.html',{'books':books,'query':q})
    else:
        return HttpResponse('Por favor sumbeta algum termo a ser pesquisado')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponseRedirect('/contact/thanks/?email='+cd['email'])
    else:
        form = ContactForm(initial={'subject': 'Site muito bom'})
    return render(request,'contact_form.html',{'form':form})

def thanks(request):
    return HttpResponse('Email enviado para %s' % request.GET['email'] )
