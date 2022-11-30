from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView

from djello.models import List, Card


class BoardView(TemplateView):
    template_name = "djello/board.html"


class CreateListView(CreateView):
    model = List
    fields = ["title"]

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponse(headers={"HX-Trigger": "AddedList"})


class CreateCardView(CreateView):
    model = Card
    fields = ["title"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list_id"] = self.kwargs.get("list_id")
        return context

    def form_valid(self, form):
        list_id = self.kwargs.get("list_id")
        form.instance.list_id = list_id
        form.save()

        return HttpResponse(headers={"HX-Trigger": f"AddedCard{list_id}"})
