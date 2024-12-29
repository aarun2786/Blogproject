from django.dispatch import receiver
from .models import Post,Bloger
from django.contrib.auth.models import User
from django.db.models.signals import pre_save,post_save




@receiver(pre_save,sender=Post)
def setSlug(sender,instance,**kwrags):
    title = instance.title
    slug = title.replace(" ","-")
    instance.slug = slug

@receiver(post_save,sender=User)
def saveBloger(sender,instance,created,**kwargs):
    if created:
        Bloger.objects.create(user=instance)
