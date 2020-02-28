from django.shortcuts import render
from .models import Subnavigator,Navconstruct,Social,Footer,Text,Footercont, Page,Slider,Pagenext, Projects, Example
from django.template.context_processors import csrf

def example(request, slug,sslug,ssslug):
    response = {}
    response.update(csrf(request))
    response['nav'] = Navconstruct.objects.all()
    if slug:
        response['page'] = [Navconstruct.objects.get(slug=slug)]
    else:
        response['page'] = None
    response['info'] = Social.objects.filter(social=False)
    if sslug:
        response['spage'] = None
    if ssslug:
        response['sspage'] = [Example.objects.get(slug=ssslug)]
    else:
        response['sspage'] = None
    response['info'] = Social.objects.filter(social=False)
    response['path0'] = [Navconstruct.objects.get(slug=slug)][0]
    response['social'] = [Social.objects.filter(social=True)]
    response['footer'] = Footer.objects.all()
    response['foot'] = Footercont.objects.all()
    response['text'] = Text.objects.all()
    response['exam'] = Example.objects.all()


    return render(request, 'bi.html', response)

def construction(request, slug,sslug='empty'):
    response = {}
    response.update(csrf(request))
    response['nav'] = Navconstruct.objects.all()
    response['subnav'] = Subnavigator.objects.all()
    if slug:
        response['page'] = [Navconstruct.objects.get(slug=slug)]
    else:
        response['page'] = None
    response['info'] = Social.objects.filter(social=False)
    if sslug:
        response['spage'] = [Subnavigator.objects.get(slug=sslug)]
    else:
        response['spage'] = None
    response['info'] = Social.objects.filter(social=False)
    response['path0'] = [Navconstruct.objects.get(slug=slug)][0]
    response['path1'] = [Subnavigator.objects.get(slug=sslug)][0]
    response['social'] = [Social.objects.filter(social=True)]
    response['footer'] = Footer.objects.all()
    response['foot'] = Footercont.objects.all()
    response['text'] = Text.objects.all()
    response['exam'] = Example.objects.all()


    return render(request, 'bi.html', response)


def main(request,slug=None):
    response = {}
    response.update(csrf(request))
    response['nav'] = Navconstruct.objects.all()
    response['subnav'] = Subnavigator.objects.all()
    if slug:
        response['page'] = [Navconstruct.objects.get(slug=slug)]
    else:
        response['page'] =None
    response['info'] = Social.objects.filter(social=False)
    response['social'] = Social.objects.filter(social=True)
    response['footer'] = Footer.objects.all()
    response['foot'] = Footercont.objects.all()
    response['text'] = Text.objects.all()
    if slug:
        response['path0'] = [Navconstruct.objects.get(slug=slug)][0]
    else:
        response['path0'] = None
    return render(request, 'bi.html', response)


# Create your views here.
