from django.db import models
from django.utils.translation import ugettext_lazy as _


class X(models.Model):

    y = models.CharField(help_text=_(''), max_length=10)
