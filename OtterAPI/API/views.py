from django.shortcuts import get_list_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from .serializers import OtterSerializer

from .models import Otter

# Create your views here.


class OtterList(generics.ListCreateAPIView):
    renderer_classes = [JSONRenderer]

    queryset = Otter.objects.all()
    serializer_class = OtterSerializer


class OtterDetail(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]

    queryset = Otter.objects.all()
    serializer_class = OtterSerializer


def index(request):
    return HttpResponse("Hey, this is the API index")
