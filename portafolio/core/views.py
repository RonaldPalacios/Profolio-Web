from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage


# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def contact(request):
    #print('tipo de peticion: {}'.format(request.method))
    
    contact_form = ContactForm
    if request.method == 'POST':
            contact_form = ContactForm(data=request.POST)
            if contact_form.is_valid():
                first_name = request.POST.get('first_name', '')
                last_name = request.POST.get('last_name', '')
                contry = request.POST.get('contry', '')
                city = request.POST.get('city', '')
                email = request.POST.get('email', '')
                descripcion = request.POST.get('descripcion', '')
                
                #enviar en email
                email = EmailMessage(
                    'Received Message from Contact',
                    'Message sent by {} {} {} {} <{}>:\n\n{}'.format(first_name, last_name, contry, city, email, descripcion ),
                    email,
                    ['afb48e30a05588@inbox.mailtrap.io'],
                    reply_to=[email],
                )
                
                try:
                   email.send()                
                   return redirect('/contact/?ok')
                except:
                    return redirect('/contact/?error')
                
    return render(request, 'core/contact.html', {'form' : contact_form})

