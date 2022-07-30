from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from webapp.forms import PollForm, UserPollForm
from webapp.models import Poll


class IndexView(ListView):
    model = Poll
    template_name = "polls/index.html"
    context_object_name = "polls"
    paginate_by = 5

    def get_queryset(self):
        return Poll.objects.all()


class PollView(DetailView):
    template_name = "polls/poll_view.html"
    model = Poll

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['interviews'] = self.object.interviews
        return context


class DeletePoll(DeleteView):
    model = Poll

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("index")


class CreatePoll(CreateView):
    form_class = PollForm
    template_name = "polls/poll_create.html"

    def form_valid(self, form):
        poll = form.save(commit=False)
        poll.save()
        form.save_m2m()
        return redirect("poll_view", pk=poll.pk)


class UserProjectForm:
    pass


class UpdatePoll(UpdateView):
    form_class = PollForm
    template_name = "polls/poll_update.html"
    model = Poll

    def get_form_class(self):
        if self.request.GET.get("is_admin"):
            return PollForm
        return UserPollForm

    def get_success_url(self):
        return reverse("poll_view", kwargs={"pk": self.object.pk})
