import re
from django.conf import settings

from django.core.mail import send_mail
from rest_framework.exceptions import ValidationError

email_regex = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b")
phone_regex = re.compile(r"(\+[0-9]+\s*)?(\([0-9]+\))?[\s0-9\-]+[0-9]+")


def email_or_phone_number(email_or_phone_number: str):
    if re.fullmatch(email_regex, email_or_phone_number):
        data = 'email'
    elif re.fullmatch(phone_regex, email_or_phone_number):
        data = 'phone'
    else:
        raise ValidationError("Invalid Email or Phone Number")
    return data

# print(email_or_phone_number('burxon@gmail.com'))


def send_email_cod(email, code):
    send_mail(
        subject="Tasdiq kodi",
        message=f"Your code: {code}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )