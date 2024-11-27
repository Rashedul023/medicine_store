from django.db import models
from django.conf import settings

class Cart(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    medicine = models.ForeignKey('store.Medicine', on_delete=models.CASCADE)  # Corrected app reference
    quantity = models.PositiveIntegerField(default=0)

    def get_total_price(self):
        return self.medicine.price * self.quantity

