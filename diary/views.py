from django.views import generic
from .forms import InquiryForm
import logging
from django.urls import reverse_lazy
logger = logging.getLogger(__name__)
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Diary

class IndexView(generic.TemplateView):
    template_name = "index.html"

class IndexView2(generic.TemplateView):
    template_name = "index2.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました')
        logger.info('Inquiry send by{}'.format(form.cleaned_data['name']))
        return super().form_valid(form)




class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary_list.html'

    def get_queryset(self):
        diaries = Diary.objects.filter(user = self.request.user).\
            order_by('-created_at')
        return diaries