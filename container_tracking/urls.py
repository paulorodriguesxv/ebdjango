from django.urls import path, register_converter

from . import views, converters

register_converter(converters.ContainerNumberConverter, "AAAADDDDDDD")

urlpatterns = [
    path('', views.index, name='index'),
    path('<AAAADDDDDDD:container_number>', views.results, name="results"),
    path('search', views.search, name='search'),
    path('feedback', views.feedback, name='feedback'),
]
