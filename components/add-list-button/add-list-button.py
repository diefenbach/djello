# In a file called [project root]/components/calendar/calendar.py
from django_components import component


@component.register("add-list-button")
class AddListButton(component.Component):
    template_name = "add-list-button/add-list-button.html"
