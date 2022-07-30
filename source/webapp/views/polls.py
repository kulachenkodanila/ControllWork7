from django.views.generic import ListView, DetailView

from webapp.models import Poll


class IndexView(ListView):
    model = Poll
    template_name = "polls/index.html"
    context_object_name = "polls"
    paginate_by = 5

    def get_queryset(self):
        return Poll.objects.all()



