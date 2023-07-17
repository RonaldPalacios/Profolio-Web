from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def contact(request):
    return render(request, 'core/contact.html')

def mail (request):
    if request.method == 'POST':
        first_name = request.POST = ['first_name']
        last_name = request.POST = ['last_name']
        contry = request.POST = ['contry']
        city = request.POST = ['city']
        email = request.POST = ['email']
        message = request.POST = ['descripcion']
        
        template = render_to_string('email.template.html', {
            'first_name': first_name,
            'last:name': last_name,
            'contry': contry,
            'city': city,
            'email': email,
            'message':message
        })
        
        email = EmailMessage(
           template,
           settings.EMAIL.HOST.USER,
           ['rpalacioso12@outlook.com']
            
        )
    
        email.fail_silently = False
        
        email.send()

        messages.success(request, 'Message sent')
        return redirect('core/contact.html')