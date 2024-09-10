from django.shortcuts import render, redirect
from .forms import RepresentativeForm
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail


def representative_form_view(request):
    if request.method == 'POST':
        form = RepresentativeForm(request.POST, request.FILES)
        if form.is_valid():
            # Process form data
            name = form.cleaned_data['name']
            state = form.cleaned_data['state']
            phone_number = form.cleaned_data['phone_number']
            occupation = form.cleaned_data['occupation']
            marital_status = form.cleaned_data['marital_status']
            monthly_income = form.cleaned_data['monthly_income']
            email = form.cleaned_data['email']

            # File uploads (front and back of the ID card)
            id_card_front = form.cleaned_data['id_card_front']
            id_card_back = form.cleaned_data['id_card_back']

            # Prepare email content
            subject = 'New Representative Form Submission'
            message = f"""
            New Representative Form Submission:

            Name: {name}
            State: {state}
            Phone Number: {phone_number}
            Occupation: {occupation}
            Marital Status: {marital_status}
            Monthly Income: {monthly_income}
            Email: {email}
            """

            # Create an email message
            email_message = EmailMessage(
                subject,  # Subject
                message,  # Message
                settings.EMAIL_HOST_USER,  # From email (configured in settings)
                ['sweetlove24500@gmail.com'],  # To email
            )

            # Attach ID card front and back (if uploaded)
            if id_card_front:
                email_message.attach(id_card_front.name, id_card_front.read(), id_card_front.content_type)

            if id_card_back:
                email_message.attach(id_card_back.name, id_card_back.read(), id_card_back.content_type)

            # Send the email
            email_message.send()

            # Redirect to the success page
            return redirect('success')

    else:
        form = RepresentativeForm()

    return render(request, 'representatives/representative_form.html', {'form': form})


def success_view(request):
    return render(request, 'representatives/success.html')
