from django.http import HttpResponse
from django.template import Template, RequestContext


def component_view(request, component_name):
    """
    View for a component without a parameter
    """
    template = Template('{% component "' + component_name + '" %}')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def component_view_1(request, component_name, param):
    """
    View for a component with one parameter
    """
    template = Template('{% component "' + component_name + '" ' + param + ' %}')
    context = RequestContext(request)
    return HttpResponse(template.render(context))
