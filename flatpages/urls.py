from django.urls import path
from . import views


app_name ="flatpages"

urlpatterns = [
    path("blogs/", views.FlatPageBlogHomeView.as_view(), name="blog_list"),
]