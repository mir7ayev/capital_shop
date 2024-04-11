from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
import requests


def contact_view(request):
    if request.method == 'POST':
        data = request.POST
        Contact.objects.create(name=data['name'],
                               message=data['message']).save()

        contact = Contact.objects.filter().last()

        token = '6486746634:AAHgQKInguR3FxhT-46JB5ap2M-L-XeYTD8'

        requests.get(f"""
                    https://api.telegram.org/bot{token}/sendMessage?chat_id=-4175535863
                    &text=Capital Shop
                    \nname: {contact.name.title()}\nmessage: {contact.message}
                    """)

        return redirect('/contact/')

    return render(request, 'contact.html')
