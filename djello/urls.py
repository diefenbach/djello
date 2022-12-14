from django.urls import path

from djello.views import (
    BoardView,
    CreateListView,
    CreateCardView,
    save_lists,
    save_list_title,
)

app_name = "djello"
urlpatterns = [
    path("", BoardView.as_view(), name="board"),
    path("create-list", CreateListView.as_view(), name="create-list"),
    path("create-card/<int:list_id>", CreateCardView.as_view(), name="create-card"),
    path("save-lists", save_lists, name="save-lists"),
    path("save-list-title/<int:list_id>", save_list_title, name="save-list-title"),
]
