from django.shortcuts import render
from .models import Subnavigator,Navconstruct,Social,Footer,Text,Footercont,Example, Faqblock, Contact, Contdecr, Textslider, Mpage, Values
from .forms import ContactForm
from django.template.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
import json





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
    response['path0'] = [Navconstruct.objects.get(slug=slug)][0]



    return render(request, 'bi.html', response)

def construction(request, slug,sslug='empty'):
    response = {}
    response.update(csrf(request))
    response['nav'] = Navconstruct.objects.all()
    response['subnav'] = Subnavigator.objects.all()
    if sslug == 'slub':
        response['faq'] = [Faqblock.objects.get(name='Deep')][0]
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
    return render(request, 'bi.html', response)


def main(request, slug = "fundament"):
    response = {}
    response.update(csrf(request))
    response['nav'] = Navconstruct.objects.all()
    response['subnav'] = Subnavigator.objects.all()
    response['Textslider'] = Textslider.objects.all()
    if slug:
        response['page'] = [Navconstruct.objects.get(slug=slug)]
    else:
        response['page'] = False
    response['info'] = Social.objects.filter(social=False)
    response['social'] = Social.objects.filter(social=True)
    response['footer'] = Footer.objects.all()
    response['foot'] = Footercont.objects.all()
    response['text'] = Text.objects.all()
    if slug == 'faq':
        response['faq'] = [Faqblock.objects.get(name='Частые вопросы и ответы')][0]
        response['projects'] = Example.objects.all()[:5]
    else:
        response['faq'] = [Faqblock.objects.get(name='Основная страница')][0]

    response['title'] = [Navconstruct.objects.get(slug="company")][0]
    if slug:
        response['path0'] = [Navconstruct.objects.get(slug=slug)][0]
    else:
        response['path0'] = False
    if slug == 'fundament':
        response['Mpage'] = [Mpage.objects.get()][0]
        response['Values'] = Values.objects.all()
        response['page'] = False
        response['path0'] = False






    return render(request, 'bi.html', response)

# Функция формы обратной связи

def contactform(reguest, slug = 'contact'):

    nav = Navconstruct.objects.all()
    page = [Navconstruct.objects.get(slug=slug)]
    contdecr = [Contdecr.objects.get()][0]
    contact = Contact.objects.all()
    info = Social.objects.filter(social=False)
    social = Social.objects.filter(social=True)
    footer = Footer.objects.all()
    foot = Footercont.objects.all()

    if slug:
        path0 = [Navconstruct.objects.get(slug=slug)][0]
    else:
        path0 = None



    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recepients = ['ugeopolimer@gmail.com']
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            ''' Begin reCAPTCHA validation 
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            
            if result['success']:
                form.save()
                messages.success(request, 'New comment added with success!')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                End reCAPTCHA validation '''

            if copy:
                recepients.append(sender)
            try:
                send_mail(subject, message, 'ugeopolimer@gmail.com', recepients)
            except BadHeaderError: #Защита от уязвимости
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            return HttpResponseRedirect('/thanks/')

    else:
        form = ContactForm()
    # Выводим форму в шаблон
    return render(reguest,'bi.html',
            {'form': form, 'info':info, 'social':social, 'footer':footer, 'foot':foot, 'path0':path0,
            'page' : page, 'nav':nav, 'contdecr' : contdecr, 'contact': contact, 'GOOGLE_RECAPTCHA_SITE_KEY': settings.GOOGLE_RECAPTCHA_SITE_KEY,})





def thanks(reguest):
    info = Social.objects.filter(social=False)
    social = Social.objects.filter(social=True)
    footer = Footer.objects.all()
    foot = Footercont.objects.all()
    path0 = [Navconstruct.objects.get(slug='fundament')][0]
    thanks = 'thanks'
    return render(reguest, 'bi.html', {'page': thanks, 'info':info, 'social':social, 'footer':footer, 'foot':foot,'path0':path0})


# Create your views here.
