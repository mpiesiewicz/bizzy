from django.db import models
from django.utils.translation import gettext as _

from .utils import get_default_payment_status
# Create your models here.


class PaymentStatuses(models.Model):

    payment_status_index = models.PositiveSmallIntegerField(
        unique=True,
        null=False,
        verbose_name=_('Payment Status Index'),
    )

    payment_status = models.CharField(
        max_length=40,
        unique=True,
        verbose_name=_("Payment Statuses")
    )

    class Meta:
        verbose_name = _('Payment Status')
        verbose_name_plural = _('Payment Statuses')

    def __str__(self):
        return self.payment_status


class EventType(models.Model):

    event_type = models.CharField(
        max_length=20,
        unique=True,
        verbose_name=_('Event Type')
    )

    class Meta:
        verbose_name = _('Event Type')
        verbose_name_plural = _('Event Types')

    def __str__(self):
        return self.event_type


class EventItem(models.Model):

    event_type = models.ForeignKey(
        EventType,
        on_delete=models.SET_NULL,
        verbose_name=_('Event Type'),
        default=None,
        blank=True,
        null=True,
        )

    title = models.CharField(max_length=200, verbose_name=_("Title"))

    # completed = models.BooleanField(default=False, verbose_name=_())

    date = models.DateTimeField(verbose_name=_('Date'))
    payment_status = models.ForeignKey(
        PaymentStatuses,
        on_delete=models.SET_NULL,
        verbose_name=_('Payment Status'),
        null=True,
        blank=True,
        default=get_default_payment_status,
        )

    class Meta:
        verbose_name = _('Event Item')
        verbose_name_plural = _('Event Items')

    def __str__(self):
        # Use _() to mark the string for translation
        return _("Event") + f": {self.title} - {self.date.strftime('%d/%m/%Y %a/%W')}"