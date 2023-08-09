from django.urls import path
from . import views

app_name = "assignments"

urlpatterns = [
    path("", views.HomeTemplateView.as_view(), name="home"),
    path("order/", views.AssignmentOrderView.as_view(), name="place_order"),
    path("weekly/", views.WeeklyAssignemntView.as_view(), name="place_weekly_order"),

]
