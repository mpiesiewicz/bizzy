from django.db.models import Min
from django.apps import apps

# def get_default_payment_status(PaymentStatuses):
#     # Check if there are any entries in the PaymentChoice model
#     if PaymentStatuses.objects.exists():
#         # Return the first item
#         return PaymentStatuses.objects.first()
#     else:
#         # Return None if there are no entries
#         return None
#


def get_default_payment_status():
    # Check if there are any entries in the PaymentStatuses model
    PaymentStatuses = apps.get_model('myapp', 'PaymentStatuses')
    if PaymentStatuses.objects.exists():
        # Get the item with the lowest payment status index
        lowest_index = PaymentStatuses.objects.aggregate(lowest_index=Min('payment_status_index'))['lowest_index']
        return PaymentStatuses.objects.get(payment_status_index=lowest_index)
    else:
        # Return None if there are no entries
        return None
