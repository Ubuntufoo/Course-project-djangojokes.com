import sendgrid
from sendgrid.helpers.mail import To, Mail

from django.conf import settings


def send_email(to, subject, content, sender='timothymurphy123@gmail.com'):
    sg = sendgrid.SendGridAPIClient(settings.SENDGRID_API_KEY)
    mail = Mail(
        from_email=sender,
        to_emails=to,
        subject=subject,
        html_content=content
    )
    return sg.send(mail)
