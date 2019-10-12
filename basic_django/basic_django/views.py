from basic_django import settings
from django.http import HttpResponse
from .tasks import send_email_task

def test_8commit(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [settings.TESTING_EMAIL,]
    from django.core.mail import send_mail
    send_mail( subject, message, email_from, recipient_list )
    html = "<html><body>Email sent</body></html>"
    return HttpResponse(html)


def celery_example_5commit(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [settings.TESTING_EMAIL,]
    from django.core.mail import send_mail
    # USING CELERY TASK for sending email Asynchronously
    #match.email_user(subject, message). This will delay the response 
    # So will do this task asynchronously using celery
    # We have created a celery task. Using it we will send the email.
    # The code does not have to wait till the email is sent
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    recipient_list = [settings.TESTING_EMAIL,]
    send_email_task.delay(recipient_list,subject,message)
    html = "<html><body>Email sent using celery</body></html>"
    return HttpResponse(html)