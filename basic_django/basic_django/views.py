<<<<<<< HEAD
from django.http import HttpResponse
import datetime


###############################
## LOGGING
import logging
logger_custom_string = logging.getLogger("custom_string")
from basic_django import settings
#logger_custom_string.debug(settings.pp_odir(locals()))
#usage:
##logger_custom_string.debug(settings.pp_odir(user_set))  # This will pretty print all the properties from dir(user_set)
#sql = str(user_set.query)
#sql = user_set.query.__str__()
##logger_custom_string.debug(settings.pp_sql_sql(sql)) # pretty print the sql obtained from the .query
##logger_custom_string.debug(settings.pp_sql_query_pg(user_set)) # pretty print the sql using mogrify only possible with Psycopg
##logger_custom_string.debug(settings.pp_sql_query_any(user_set)) # pretty print the sql using EXPLAIN. But runs extra sql
#import traceback
##logger_custom_string.debug(settings.pp_traceback(traceback.format_stack())) #test traceback
logger_database = logging.getLogger("django.db.backends")
#usage:
#logger_database.filters[0].open()
#logger_database.filters[0].close()
=======
from basic_django import settings
from django.http import HttpResponse

def test_8commit(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [settings.TESTING_EMAIL,]
    from django.core.mail import send_mail
    send_mail( subject, message, email_from, recipient_list )
    html = "<html><body>Email sent</body></html>"
    return HttpResponse(html)
>>>>>>> 6b6f965... FOURTH COMMIT: creating new gmail account, use 2 step verification, create app password, DJANO email config, view to send email
