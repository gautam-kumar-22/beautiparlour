"""Extra functionality."""
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

def send_email_to_admin(ctx):
	"""Send email."""
	subject = 'Beaurty parlor info'
	from_email = ctx.get('email')
	to_email = ''
	context = {
		'name': ctx.get('name'),
		'phone_number': ctx.get('phone_number'),
		'address': ctx.get('address'),
		'message': ctx.get('message'),
	}
	message = render_to_string('email.html', context)
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
	msg.attach_alternative(message, "text/html")
	msg.content_sub_type = 'html'
	msg.send()
