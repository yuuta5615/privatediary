from django.views import generic
from .forms import InquiryForm

class IndexView(generic.TemplateView):
    template_name = "index3.html"

class InquiryView(generic.FormView):
    template_name = "inquiry2.html"
    form_class = InquiryForm

