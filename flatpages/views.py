from django.shortcuts import render
from django.views import generic


class FlatPageBlogHomeView(generic.TemplateView):
    template_name= "flatpages/blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    