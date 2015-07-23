from django.template import RequestContext
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail

from .forms import ContactForm


def contact_form(request):
	if request.POST:
		form = ContactForm(request.POST)
		if form.is_valid():

			subject = request.POST.get('subject', '')
			message = request.POST.get('message', '')
			from_email = request.POST.get('from_email', '')
			subject = form.cleaned_data['subject']
			receiver = form.cleaned_data['email']

			try:
				send_mail(subject, message, from_email, [settings.EMAIL_HOST_USER])
			except BadHeaderError:
				return render(request, 'contact.html', {'form':form},context_instance=RequestContext(request))
			return HttpResponseRedirect('/contact/thank-you/')
			
		else:
			return render(request, 'contact.html', {'form':form},context_instance=RequestContext(request))
	else:
		form = ContactForm()
		return render(request, 'contact.html', {'form':form},context_instance=RequestContext(request))

def thank_you(request):
	return render(request, 'thankyou.html')