from django.views.generic.edit import CreateView
from .forms import FeedbackCreateForm
from .models import Feedback
from .utils import get_client_ip, send_contact_email_message


class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackCreateForm
    template_name = 'feedback/feedback.html'
    success_url = '.'

    def form_valid(self, form):
        feedback = form.save(commit=False)
        feedback.ip_address = get_client_ip(self.request)
        send_contact_email_message(feedback.subject, feedback.email, feedback.content)
        return super().form_valid(form)
