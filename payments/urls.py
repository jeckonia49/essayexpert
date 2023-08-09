from django.urls import path
from . import views

app_name="payments"

urlpatterns = [
    path("<int:pk>/<str:slug>/", views.TransactionView.as_view(), name="payments_order_detail"),
    # path("", views.name, name="payments_order_detail"),
]