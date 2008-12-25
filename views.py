from django.http import HttpResponseRedirect
import models

def slotshow(request, slot_id):
    banner = models.Banner.objects.filter(slot=slot_id).order_by('?')[0]
    return HttpResponseRedirect(banner.image.url)
