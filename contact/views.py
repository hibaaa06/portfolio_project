from django.shortcuts import render, redirect
from .models import ContactMessage
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name','').strip()
        email = request.POST.get('email','').strip()
        message = request.POST.get('message','').strip()
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, "Message sent — thank you!")
            return redirect('contact')
        else:
            messages.error(request, "Please fill all fields.")
    return render(request, 'contact/contact.html')
