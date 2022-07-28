from django.urls import path

from . import views

app_name = "otters"
urlpatterns = [
    path("", views.index, name="index"),
    path("all", views.get_all, name="get_all"),
    path("name/<str:name>/", views.get_by_name, name="get_by_name"),
    path("age/<int:age>/", views.get_by_age, name="get_by_age"),
    path("sex/<str:sex>/", views.get_by_sex, name="get_by_sex"),
    path("post/", views.create_form, name="create_form"),
    path("create/", views.create_otter, name="create_otter"),
]
