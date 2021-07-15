from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def Index (request):
    return render(request,'index.html')

def About (request): 
    return render(request,'about.html')

def Contact(request): 
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        subject = f'From Employee Management System, {subject}'
        body = f'Hi Admin, \n \n \t {name} is trying to contact you. \nEmail: {email} \n Message: {message} \n\nThanks, \nFood Ordering System Service'
        from_email = settings.EMAIL_HOST_USER
        to_email = ['pilusahoo14@gmail.com']
        send_mail(subject, body, from_email, to_email, fail_silently=True)
        sub1 = "From Employee Management System"
        body1 = "Thanks for contacting us. We will get back to you within 48 hrs."
        send_mail(sub1, body1, from_email, [email], fail_silently=True)
    return render(request,'contact.html')

def Services (request): 
    return render(request,'services.html')