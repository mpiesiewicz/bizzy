from django.contrib import admin
from .models import PaymentStatuses, EventType, EventItem


# Register your models here.
admin.site.register(EventItem)
admin.site.register(PaymentStatuses)
admin.site.register(EventType)