from django.shortcuts import render
import netCDF4
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader

def index(request):
    return render(request, 'index.html')

def plot_lightning(request):
    if request.method == 'POST':
        latitude = float(request.POST.get('latitude'))
        longitude = float(request.POST.get('longitude'))

        # Read data
        wlgc_density = np.load("/Users/andrewondara/lightning-webapp/lightning_webapp/lightning_webapp/data/wlgc_lightning_mean.npy")
        wlgc_lat = np.load("/Users/andrewondara/lightning-webapp/lightning_webapp/lightning_webapp/data/wlgc_lat.npy")
        # Calculate average lightning density at each latitude


        # Create scatter plot
        plt.figure(figsize=(10, 6))
        plt.scatter(wlgc_lat, wlgc_density, marker='o')
        plt.xlabel('Latitude')
        plt.ylabel('Lightning Density')
        plt.title(f'Lightning Density at Latitude {latitude} and Longitude {longitude}')
        plt.grid(True)

        # Save the plot to a file
        plot_file_path = '/Users/andrewondara/lightning-webapp/lightning_webapp/lightningapp/static/plot.png'
        plt.savefig(plot_file_path)

        # Close the plot to prevent memory leaks
        plt.close()

        # Render the template with the plot
        template = loader.get_template('/Users/andrewondara/lightning-webapp/lightning_webapp/lightningapp/templates/index.html')
        context = {'plot_file_path': plot_file_path}
        return HttpResponse(template.render(context, request))

    return HttpResponseBadRequest()
