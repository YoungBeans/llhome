from django.urls import path
from . import views
urlpatterns = [
    path('', views.board_create, name="board_create"),
    path('view/', views.board_view, name="board_view"),
    path('<int:pk>/', views.board, name="board"),
    path('update/<int:pk>', views.board_update, name="board_update"),
    path('delete/<int:pk>', views.board_delete, name="board_delete"),
]
