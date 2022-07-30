from django.urls import path

from webapp.views.choices import CreateChoiceView
from webapp.views.polls import IndexView, PollView, DeletePoll, CreatePoll, UpdatePoll

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('poll/<int:pk>/', PollView.as_view(), name="poll_view"),
    path('poll/<int:pk>/delete/', DeletePoll.as_view(), name="delete_poll"),
    path('poll/add/', CreatePoll.as_view(), name="create_poll"),
    path('poll/<int:pk>/update/', UpdatePoll.as_view(), name="update_poll"),
    path('poll/<int:pk>/choice/add/', CreateChoiceView.as_view(), name="poll_choice_create"),

]
