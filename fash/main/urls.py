from django.urls import path
from . import views

urlpatterns=[
path("", views.index, name="index"),
path("pred", views.pred, name="pred"),
path("tags", views.tags, name="tags"),
path("v1/", views.v1, name="view 1"),
path("pyfun",views.pyfun)
]