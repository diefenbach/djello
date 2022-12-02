import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
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
        form.instance.order = 100000
        form.save()

        list_ = List.objects.get(pk=list_id)
        for i, card in enumerate(list_.cards.all()):
            card.order = i * 10
            card.save()

        return HttpResponse(headers={"HX-Trigger": f"AddedCard{list_id}"})


@csrf_exempt
def store_lists(request):
    data = json.loads(request.body.decode("utf-8"))

    for i, card_id in enumerate(data.get("cards", [])):
        card = Card.objects.get(pk=card_id)
        card.list_id = data.get("list")
        card.order = i * 10
        card.save()

    return HttpResponse()
