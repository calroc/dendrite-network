import logging
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from dendnet.stores import url2tag, tag2url
from spreadlogger import SpreadHandler


log = logging.getLogger('mon')
try:
    log.addHandler(SpreadHandler())
except:
    log.exception("Spread Logging NON-active.")


def home(request):
    return render_to_response('index.html', context_instance=RequestContext(request))
def describe(request):
    return render_to_response('describe.html', context_instance=RequestContext(request))
def d3demo(request):
    return render_to_response('d3demo1.html', context_instance=RequestContext(request))


def register(request):
    if request.method != 'POST':
        return render_to_response(
            'register.html',
            context_instance=RequestContext(request),
            )

    url = request.POST.get('urly')
    assert url
    tag = url2tag(url)
    log.info('register %s %r', tag, url)
    return render_to_response(
        'register.html',
        dict(tag=tag),
        context_instance=RequestContext(request),
        )


def bump(request, me, it, you):
    data = dict(
        from_url=tag2url(me),
        iframe_url=tag2url(it),
        your_url=tag2url(you),
        me=me,
        it=it,
        you=you,
        )
    log.info('bump %s %s %s', me, it, you)
    return render_to_response(
        'bump.html',
        data,
        context_instance=RequestContext(request),
        )


def engage(request, me, it):
    log.info('engage %s %s', me, it)
    return HttpResponse('true', mimetype="application/json")





