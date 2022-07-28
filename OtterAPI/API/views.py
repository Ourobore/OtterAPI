from django.shortcuts import get_list_or_404, render
from django.http import Http404, HttpResponse
from django.template import loader

from .models import Otter

# Create your views here.
def index(request):
    return HttpResponse("Hey, this is the API index")


def get_infos(request, otter):
    return str(f"{otter.name} ({otter.sex}): {otter.age} years old.")


def get_by_name(request, name):
    otters = get_list_or_404(Otter, name=name)
    return render(request, "otters/summary.html", {"otters": otters})


def get_by_age(request, age):
    return HttpResponse(Otter.objects.filter(age=age))


def get_by_sex(request, sex):
    return HttpResponse(Otter.objects.filter(sex=sex))


def get_all(request):
    context = {"otters": Otter.objects.all()}
    return render(request, "otters/index.html", context)


def create_form(request):
    return render(request, "otters/create_otter.html")


def create_otter(request):
    if request.method == "POST":
        otter = Otter(
            name=request.POST["name"],
            age=request.POST["age"],
            sex=request.POST["sex"],
        )
        otter.save()

    return HttpResponse("Nothing to see")
