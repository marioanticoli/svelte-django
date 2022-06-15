from django.urls import re_path
from django.views.generic import TemplateView

urlpatterns = [
    re_path('blog', TemplateView.as_view(template_name='blog.html')),
    # Home must be the last line
    re_path('', TemplateView.as_view(template_name='index.html')),
]
