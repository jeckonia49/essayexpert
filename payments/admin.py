from django.contrib import admin
from .models import Transaction
# Register your models here.

@admin.register(Transaction)
class AdminTransaction(admin.ModelAdmin):
    list_display = [
        "client",
        "order",
        "price",
        "createdAt",
        "completed",
        "failed",
    ]
    list_filter = [
        "client",
        "order",
        "completed",
        "failed",
    ]

