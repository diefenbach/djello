from django.urls import path, re_path

from components_helper.views import component_view, component_view_1

app_name = 'c'
urlpatterns = [
    path("component/<str:component_name>", component_view, name="c"),
    path("component/<str:component_name>/<str:param>", component_view_1, name="c1"),
    # re_path(r"component/(?P<component_name>\w+)/(?P<params>[-/\w*]*)", component_view_1, name="c2"),
]
