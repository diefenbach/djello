from django_components import component

from djello.models import List


@component.register("list-editable-title")
class ListEditableTitle(component.Component):
    template_name = "list-editable-title/list-editable-title.html"

    def get_context_data(self, list_id=None):
        list_ = List.objects.get(pk=list_id)
        return {
            "list": list_,
        }
