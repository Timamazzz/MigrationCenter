from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
    return ip


def send_contact_email_message(subject, email, content):
    message = render_to_string('feedback/feedback_email_send.html', {
        'subject': subject,
        'email': email,
        'content': content,
    })
    email = EmailMessage("Обратная связь Цпп", message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
    email.send(fail_silently=False)

