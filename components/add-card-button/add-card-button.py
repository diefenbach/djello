# In a file called [project root]/components/calendar/calendar.py
from django_components import component


@component.register("add-card-button")
class AddListButton(component.Component):
    template_name = "add-card-button/add-card-button.html"

    def get_context_data(self, list_id=None):
        return {
            "list_id": list_id,
        }
