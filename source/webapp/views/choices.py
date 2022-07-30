from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import ChoiceForm
from webapp.models import Poll


class CreateChoiceView(CreateView):
    form_class = ChoiceForm
    template_name = "choices/choice_create.html"

    def form_valid(self, form):
        interview = get_object_or_404(Poll, pk=self.kwargs.get("pk"))
        form.instance.interview = interview
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("poll_view", kwargs={"pk": self.object.interview.pk})

