

from oscar.apps.customer.forms import EmailUserCreationForm
from nocaptcha_recaptcha.fields import NoReCaptchaField


class MyEmailUserCreationForm(EmailUserCreationForm):
    captcha = NoReCaptchaField()


EmailUserCreationForm = MyEmailUserCreationForm