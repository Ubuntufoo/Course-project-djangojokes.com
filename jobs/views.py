from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import JobApplicationForm


class JobAppView(FormView):
    template_name = 'jobs/joke_writer.html'
    form_class = JobApplicationForm
    success_url = reverse_lazy('jobs:thanks')


class JobAppThanksView(TemplateView):
    template_name = 'jobs/thanks.html'
