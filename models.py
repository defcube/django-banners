from django.db import models

class Slot(models.Model):
    name = models.CharField(max_length=255)
    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('banners_slotshow', args=[self.pk])
    def __str__(self):
        return 'Banner Slot "%s"' % self.name

class Banner(models.Model):
    slot = models.ForeignKey(Slot)
    image = models.ImageField(upload_to='uploads/%y/%j/%H/%M%S/')