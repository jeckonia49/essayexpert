from django.db import models
from accounts.models import Profile


from assignments.models import Order


class Transaction(models.Model):
    client = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True, related_name="user_payment")
    email_address = models.EmailField(max_length=255, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_payment")
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    createdAt = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    failed = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"Order: {self.order.topic} by {self.client}"
    
