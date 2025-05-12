from django.shortcuts import render
from .models import Data
import plotly.express as px
import pandas as pd

# Create your views here.
def homePage(request):
    countries = list(Data.objects.values_list('country', flat=True))
    countries = list(set(countries))
    country_count = []
    for country in countries:
        country_count.append(Data.objects.filter(country=country).count())

    print(countries)

    df = pd.DataFrame({'countries':countries, 'country_count':country_count})

    fig1 = px.bar(df, x='countries', y='country_count')
    graph1 = fig1.to_html()

    fig2 = px.pie(df, values='country_count', names='countries', title='BLAH BLAH')
    graph2 = fig2.to_html()

    return render(request, 'index.html', {'graph1': graph1, 'graph2':graph2})

def scatterPlot(request):

    if request.method == 'POST':
        x = list(Data.objects.values_list(request.POST['X'], flat=True))
        y = list(Data.objects.values_list(request.POST['Y'], flat=True))
        
        scatter_plot = px.scatter(x=x, y=y)
        scatter_plot.update_layout(
        title=f"{request.POST['X'].upper()} v/s {request.POST['Y'].upper()}",
        title_x=0.5,
        xaxis_title=request.POST['X'].upper(),
        yaxis_title=request.POST['Y'].upper(),
        showlegend=True,
        )

        scatter_plot = scatter_plot.to_html()

        return render(request, 'scatter.html', {'scatter_plot':scatter_plot})
    return render(request, 'scatter.html')

def histogramPlot(request):
    if request.method == "POST":
        if request.POST['column'] != "":
            histogram = px.histogram(pd.Series(list(Data.objects.values_list(request.POST['column'], flat=True))))
            histogram.update_layout(
                title=f"{request.POST['column'].upper()}",
                title_x=0.5,
                xaxis_title=request.POST['column'].upper(),
                yaxis_title="Frequency".upper(),
                showlegend=False,
            )
            histogram = histogram.to_html()
            return render(request, 'histogram.html', {'histogram':histogram})
    return render(request, 'histogram.html')

def piechartPlot(request):
    if request.method == "POST":
        px.pie()