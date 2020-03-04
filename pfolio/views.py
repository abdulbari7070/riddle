from django.shortcuts import render
from django.core.mail import send_mail
from portfolio.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage

# Create your views here.

from django.views.generic import ListView, DetailView
from .models import Pfolio,About,Contact
from .forms import ContactForm

class PfolioList(ListView):
    model = Pfolio

def about_view(request):
    model =  About.objects.all()[0]
    return render(request, "about.html",context={"model":model}) 

def send_custom_mail(subject, message, sender, receiver):
    msg = EmailMessage(subject, message, sender, receiver)
    msg.content_subtype = "html"  # Main content is now text/html
    return msg.send()

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        form_name = request.POST['name']
        form_email = request.POST['email']
        form_subject = request.POST['subject']
        form_message = request.POST['message']
        contact_form = Contact()
        contact_form.name = form_name
        contact_form.email = form_email
        contact_form.subject = form_subject
        contact_form.message = form_message
        contact_form.save()
        message = "<html><body><h3>Name: "+form_name+"</h3><h3>Email: "+form_email+"</h3><h3>Subject: "+form_subject+"</h3><h3>Message: "+form_message+"</h3></body></html>"
        send_custom_mail('Riddle - Contact Form', message, EMAIL_HOST_USER, [EMAIL_HOST_USER])
        # if form.is_valid():
        form = ContactForm()
        return render(request, 'contact.html', context={'message':'Form Submitted Successfully!','form': form})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def home_view(request):
    model =  Pfolio.objects.order_by("?")[:6]
    return render(request, "home.html",context={"model":model}) 