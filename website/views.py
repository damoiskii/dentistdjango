from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
    context = {

    }
    return render(request, 'website/index.html', context)


def about(request):
    context = {

    }
    return render(request, 'website/about.html', context)


def pricing(request):
    context = {

    }
    return render(request, 'website/pricing.html', context)


def service(request):
    context = {

    }
    return render(request, 'website/service.html', context)


def contact(request):
    # The method whenever a there is a form on the page to fill out...
    if request.method == "POST":
        # This is how to get the information from the form on the frontend to the backend...
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # Set up to send an email...
        send_mail(
            # 'Make Appointment',  # Subject
            message_name,  # Name
            message,  # Message
            message_email,  # From email
            ['moimyazz@gmail.com'],  # To email
        )

        context = {
            'message_name': message_name,
            'message_email': message_email,
            'message': message,
        }
        return render(request, 'website/contact.html', context)
    else:
        context = {

        }
        return render(request, 'website/contact.html', context)


def appointment(request):
    # The method whenever a there is a form on the page to fill out...
    if request.method == "POST":
        # This is how to get the information from the form on the frontend to the backend...
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']

        # This appointment variable will be the message part of the email to send...
        appointment = f'Name: {your_name}\nPhone: {your_phone}\nEmail: {your_email}\nAddress: {your_address}\nSchedule: {your_schedule}\nDate: {your_date}\nMessage: {your_message}\n'

        # Set up to send an email...
        send_mail(
            'Appointment Request',  # Subject
            appointment,  # Message
            your_email,  # From email
            ['damomyers20@gmail.com'],  # To email
        )

        context = {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_schedule': your_schedule,
            'your_date': your_date,
            'your_message': your_message,
        }
        return render(request, 'website/appointment.html', context)
    else:
        context = {

        }
        return render(request, 'website/index.html', context)
