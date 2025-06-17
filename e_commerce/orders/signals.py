from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order


@receiver(post_save, sender=Order)
def notify_admin_about_order(sender, instance, created,**kwargs):
    from django.core.mail import EmailMultiAlternatives
    from django.template.loader import render_to_string
    from django.conf import settings
    from django.contrib.auth.models import User
    from django.contrib.sites.models import Site

    current_site=Site.objects.get_current()
    domain=f"http://{current_site.domain}"


    if created:
        return 

    html_content = render_to_string(
        "emails/notify_order_created.html",
        context={"order": instance,"domain":domain},
    )

    text_content = f"New order by  {instance.first_name} {instance.last_name}"

    emails = [
        admin.email
        for admin in User.objects.filter(is_staff=True, is_superuser=True).all()
    ]
    print("Admins to call: ", emails)

    msg = EmailMultiAlternatives(
        f"Created new order {instance.id}",
        text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=emails,
    )

    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print("Sended notify to admins!")