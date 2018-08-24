from djano.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name, receiver):
    subject = 'Welcome to blood connect!'
    sender = 'developervictor8504@gmail.com'

    text_context = render_to_string('email/newsemail.txt', { "name" : name })
    html_content = render_to_string('email/newsemail.html', { "name" : name })

    msg = EmailMultiAlternatives(subject, text_content, sender, [receiver])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()