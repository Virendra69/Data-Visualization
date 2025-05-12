from django.urls import path
from .views import *

urlpatterns = [
    path('', homePage, name="homePage"),
    path('scatter/', scatterPlot, name='scatterPlot'),
    path('histogram/', histogramPlot, name='histogramPlot'),
]
