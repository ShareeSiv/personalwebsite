from django import forms
from .models import ContactProfile
from django_recaptcha.fields import ReCaptchaField

class ContactForm(forms.ModelForm):

	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '',
			}))
	email = forms.EmailField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '',
			}))
	subject = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '',
			}))
	message = forms.CharField(max_length=2000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': 'Write your message here',
			'rows': 3,
			}))
	captcha = ReCaptchaField()

	class Meta:
		model = ContactProfile
		fields = ('name', 'email', 'subject' ,'captcha','message',)