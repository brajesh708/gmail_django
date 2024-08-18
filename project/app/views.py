from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import send_mass_mail

# Create your views here.
def home(request):
    subject="Test_Mail from Django Server"
    message="This is a Demo-test mail"
    from_email="brajeshmewada694@gmail.com"
    recipient_list=["suryagurjar781@gmail.com","padlisehor@gmail.com"]
    send_mail(subject,message,from_email,recipient_list)

    return HttpResponse("please check your New_email")


# from django.shortcuts import render
# from django.http import HttpResponse
# from django.core.mail import send_mail

# def home(request):
#     subject = "Test Mail from Django Server"
#     message = "This is a Demo-test mail"
#     from_email = None
#     recipient_list = ["padlisehor@gmail.com"]
#     send_mail(subject, message, from_email, recipient_list)
#     return HttpResponse("Please check your email.")