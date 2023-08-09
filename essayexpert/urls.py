from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from django.contrib.flatpages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("assignments.urls", namespace="assignments")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("payments/", include("payments.urls", namespace="payments")),
    path("pages/", include("flatpages.urls", namespace="flatpages")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
