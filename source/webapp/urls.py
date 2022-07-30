from django.urls import path

from webapp.views.polls import IndexView, PollView, DeletePoll, CreatePoll

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('poll/<int:pk>/', PollView.as_view(), name="poll_view"),
    path('poll/<int:pk>/delete/', DeletePoll.as_view(), name="delete_poll"),
    path('poll/add/', CreatePoll.as_view(), name="create_poll"),

]
