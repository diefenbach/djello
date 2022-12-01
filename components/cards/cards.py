# In a file called [project root]/components/calendar/calendar.py
from django_components import component

from djello.models import Card


@component.register("cards")
class Lists(component.Component):
    template_name = "cards/cards.html"

    def get_context_data(self, list_id):
        return {
            "cards": Card.objects.filter(list__id=list_id),
            "list_id": list_id,
        }
