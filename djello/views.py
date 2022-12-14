from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, CreateView

from components_helper.views import component_view_1
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
def save_lists(request):
    for i, card_id in enumerate(request.POST.getlist("card")):
        card = Card.objects.get(pk=card_id)
        card.list_id = request.POST.get("list")
        card.order = i * 10
        card.save()

    return HttpResponse()


@csrf_exempt
def save_list_title(request, list_id):
    list_ = List.objects.get(pk=list_id)
    list_.title = request.POST.get("title")
    list_.save()

    # Good example of returning a component after something happens before
    # (saved the list title in this case).
    return component_view_1(request, "list-editable-title", str(list_id))
