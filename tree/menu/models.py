from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_('Menu name'))

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100, unique=100, verbose_name=_('Item name'))
    url = models.CharField(max_length=200, blank=True, null=True, verbose_name=_("URL"))
    named_url = models.CharField(max_length=200, blank=True, null=True, verbose_name=_("Named URL"))
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE,
                               verbose_name=_("Parent Item"))

    def get_url(self):
        if self.named_url:
            return reverse(self.named_url)
        return self.url

    def __str__(self):
        return self.name