from django.shortcuts import render
from django.contrib import messages
from .models import (
		Project,
	)
from django.views import generic
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from . forms import ContactForm

# Create your views here.

class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		project = Project.objects.filter(is_active=True)
		
		context["project"] = project
		return context


class ContactView(generic.FormView):
	template_name = "main/contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form): 
		form.save()

		name = form.cleaned_data['name']
		email = form.cleaned_data['email']
		subject = form.cleaned_data['subject']
		message = form.cleaned_data['message']

		# Send email
		send_mail(
			subject,
			f"From: {name} <{email}>\n\n{message}",
			settings.EMAIL_HOST_USER,  
			[settings.EMAIL_HOST_USER],  
			fail_silently=False,
		)

		messages.success(self.request, 'Thank you. I will be in touch soon.')
		return super().form_valid(form)


class ProjectView(generic.ListView):
	model = Project
	template_name = "main/project.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)

class ProjectDetailView(generic.DetailView):
	model = Project
	template_name = "main/project-detail.html"
