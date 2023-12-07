from importlib import import_module

from django.core.mail import EmailMultiAlternatives
from django.template.defaultfilters import slugify as django_slugify
from django.template.loader import render_to_string
from unidecode import unidecode


def slugify(s):
    """Translate unicode into closest possible ascii chars before slugifying."""
    return django_slugify(unidecode(str(s)))


def unique_slug(manager, slug_field, slug):
    """Ensure slug is unique for the given manager, appending a digit if it isn't."""
    max_length = manager.model._meta.get_field(slug_field).max_length
    slug = slug[:max_length]
    i = 0
    while True:
        if i > 0:
            if i > 1:
                slug = slug.rsplit("-", 1)[0]
            # We need to keep the slug length under the slug fields max length. We need to
            # account for the length that is added by adding a random integer and `-`.
            slug = "{}-{}".format(slug[:max_length - len(str(i)) - 1], i)
        if not manager.filter(**{slug_field: slug}):
            break
        i += 1
    return slug


def split_choices(choices_string):
    """Convert a comma separated choices string to a list."""
    return [x.strip() for x in choices_string.split(",") if x.strip()]


def html5_field(name, base):
    """
    Return object base with input_type attribude.

    Takes a Django form field class and returns a subclass of
    it with the given name as its input type.
    """
    return type("", (base,), {"input_type": name})


def import_attr(path):
    """
    Import attribute from path.

    Given a a Python dotted path to a variable in a module,
    imports the module and returns the variable in it.
    """
    module_path, attr_name = path.rsplit(".", 1)
    return getattr(import_module(module_path), attr_name)


def send_mail_template(subject, template, from_email, recipient_list,
                       fail_silently=False, attachments=None, context=None,
                       connection=None, headers=None):
    context = context or {}
    recipient_list = [recipient_list] if isinstance(recipient_list, str) else recipient_list

    body = render_to_string('email_extras/{}.{}'.format(template, 'txt'), context)
    html_body = render_to_string('email_extras/{}.{}'.format(template, 'html'), context)

    email = EmailMultiAlternatives(
        subject=subject,
        body=body,
        from_email=from_email,
        to=recipient_list,
        connection=connection,
        attachments=attachments,
        headers=headers,
    )
    email.attach_alternative(html_body, 'text/html')
    email.send(fail_silently)
