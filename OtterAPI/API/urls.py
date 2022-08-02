from django.urls import path

from . import views

app_name = "otters"
urlpatterns = [
    path("", views.index, name="index"),
    path("otters/", views.OtterList.as_view()),
    path("otters/<int:pk>/", views.OtterDetail.as_view()),
]
