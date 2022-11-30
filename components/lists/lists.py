# In a file called [project root]/components/calendar/calendar.py
from django_components import component

from djello.models import List


@component.register("lists")
class Lists(component.Component):
    template_name = "lists/lists.html"

    def get_context_data(self):
        return {
            "lists": List.objects.all(),
        }
