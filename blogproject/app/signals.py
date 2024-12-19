from django.dispatch import receiver
from .models import Post
from django.db.models.signals import pre_save




@receiver(pre_save,sender=Post)
def setSlug(sender,instance,**kwrags):
    title = instance.title
    slug = title.replace(" ","-")
    instance.slug_fiedl = slug



