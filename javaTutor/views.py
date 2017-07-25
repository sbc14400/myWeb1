
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, render_to_response, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login
import json

# Create your views here.

def javatutor_demo1(request, template='demo1/demo1.html'):
    return render(request, template)

def javatutor_demo2(request, template='demo1/demo2.html'):
    return render(request, template)

def javatutor_demo3(request, template='demo1/demo3.html'):
    return render(request, template)

def javatutor_demo4(request, template='demo1/demo4.html'):
    return render(request, template)

def javatutor_demo5(request, template='demo1/demo5.html'):
    return render(request, template)

def javatutor_demo21(request, template='demo2/demo21.html'):
    return render(request, template)

def javatutor_demo22(request, template='demo2/demo22.html'):
    return render(request, template)

def javatutor_demo23(request, template='demo2/demo23.html'):
    return render(request, template)

def javatutor_demo24(request, template='demo2/demo24.html'):
    return render(request, template)

def javatutor_demo25(request, template='demo2/demo25.html'):
    return render(request, template)

def javatutor_demo26(request, template='demo2/demo26.html'):
    return render(request, template)

def javatutor_demo27(request, template='demo2/demo27.html'):
    return render(request, template)

def javatutor_demo28(request, template='demo2/demo28.html'):
    return render(request, template)

def javatutor_demo31(request, template='demo3/demo31.html'):
    return render(request, template)

def javatutor_demo32(request, template='demo3/demo32.html'):
    return render(request, template)

def javatutor_demo33(request, template='demo3/demo33.html'):
    return render(request, template)

def javatutor_demo34(request, template='demo3/demo34.html'):
    return render(request, template)

def javatutor_demo41(request, template='demo4_node/demo41.html'):
    return render(request, template)

def javatutor_demo42(request, template='demo4_node/demo42.html'):
    return render(request, template)

def javatutor_demo43(request, template='demo4_node/demo43.html'):
    return render(request, template)

def javatutor_demo44(request, template='demo4_node/demo44.html'):
    return render(request, template)

def javatutor_demo45(request, template='demo4_node/demo45.html'):
    return render(request, template)

def javatutor_demo46(request, template='demo4_node/demo46.html'):
    return render(request, template)

def javatutor_demo47(request, template='demo4_node/demo47.html'):
    return render(request, template)

def javatutor_demo51(request, template='demo5_event/demo51.html'):
    return render(request, template)

def javatutor_demo52(request, template='demo5_event/demo52.html'):
    return render(request, template)

def javatutor_demo53(request, template='demo5_event/demo53.html'):
    return render(request, template)

def javatutor_demo54(request, template='demo5_event/demo54.html'):
    return render(request, template)

def javatutor_demo55(request, template='demo5_event/demo55.html'):
    return render(request, template)

def javatutor_demo56(request, template='demo5_event/demo56.html'):
    return render(request, template)

def javatutor_demo57(request, template='demo5_event/demo57.html'):
    return render(request, template)

def javatutor_demo58(request, template='demo5_event/demo58.html'):
    return render(request, template)

def javatutor_demo61(request, template='demo6_Ajax JSON/demo61.html'):
    return render(request, template)

def javatutor_demo62(request, template='demo6_Ajax JSON/demo62.html'):
    return render(request, template)

def javatutor_demo63(request, template='demo6_Ajax JSON/demo63.html'):
    return render(request, template)


def javatutor_git_anywhere(request, template='djangoNote/git_pythonanywhere.html'):
    return render(request, template)

def mygetview(request):
    if request.method == 'GET':
        print("**get**")
        data = request.GET['mydata']
        astr = "<html><b> you sent a get request </b> <br> returned data: %s</html>" % data
        return HttpResponse(astr)
    return render(request)


def mypostview(request):
    if request.method == 'POST':
        print("**post**")
        data = request.POST['mydata']
        astr = "<html><b> you sent a post request </b> <br> returned data: %s</html>" % data
        return HttpResponse(astr)
    return render(request)


def myajaxview(request):
    if request.method == 'POST':
        if request.is_ajax():
            print("**ajax post**")
            data = request.POST['mydata']
            astr = "<html><b> you sent an ajax post request </b> <br> returned data: %s</html>" % data
            return HttpResponse(astr)
    return render(request)


def myajaxformview(request):
    if request.method == 'POST':
        if request.is_ajax():
            import json

            print("**ajax form post**")
            for k, v in request.POST.items():
                print(k, v)

            print("field1 data: %s" % request.POST['field1'])
            print("field2 data: %s" % request.POST['field2'])

            mydata = [{'foo': request.POST['field1'], 'baz': request.POST['field2']}]
            return HttpResponse(json.dumps(mydata))     #, mimetype="application/json")

    return render(request)
