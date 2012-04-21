import logging
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from dendnet.stores import url2tag, tag2url, note_engage


log = logging.getLogger('mon')


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
    log.info('bump %s %s %s', me, it, you)
    return render_to_response(
        'bump.html',
        dict(
            from_url=tag2url(me),
            iframe_url=tag2url(it),
            me=me,
            it=it,
            you=you,
            ),
        context_instance=RequestContext(request),
        )


def engage(request, me, it):
    log.info('engage %s %s', me, it)
    note_engage(me, it)
    return HttpResponse('true', mimetype="application/json")




