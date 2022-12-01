from django.urls import path

from djello.views import BoardView, CreateListView, CreateCardView

app_name = "djello"
urlpatterns = [
    path("", BoardView.as_view(), name="board"),
    path("create-list", CreateListView.as_view(), name="create-list"),
    path("create-card/<int:list_id>", CreateCardView.as_view(), name="create-card"),
]
