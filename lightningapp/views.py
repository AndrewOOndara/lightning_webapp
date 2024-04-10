from django.shortcuts import render
import netCDF4
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
import os
import scipy.io as sio
import cartopy.crs as ccrs
import cartopy.feature as cfeature


def index(request):
    return render(request, 'index.html')

TRACE = "TRACE"
FAMOUS = "FAMOUS"
LOVECLIM = "LOVECLIM"

# REPLACE WITH PATH TO FILE WITH NPY FILES
pathToData = "/Users/andrewondara/lightning-webapp/lightning_webapp/data/"
# [variable, latitude, longitude, time]
dataset_files_loveclm = [
    np.load('/Users/andrewondara/lightning-webapp/lightning_webapp/lightning_webapp/data/fa_rolling_avg_with_latlon.npy'),
    np.load('/Users/andrewondara/lightning-webapp/lightning_webapp/lightning_webapp/data/lc_time_rolling')
]

dataset_files_trace = [
    np.load('/Users/andrewondara/lightning-webapp/lightning_webapp/lightning_webapp/data/tr_rolling_avg_with_latlon'),
    np.load('/Users/andrewondara/lightning-webapp/lightning_webapp/lightning_webapp/data/tr_time_rolling')
]

dataset_files_famous = [
    np.load('/Users/andrewondara/lightning-webapp/lightning_webapp/lightning_webapp/data/fa_rolling_avg_with_latlon'),
    np.load('/Users/andrewondara/lightning-webapp/lightning_webapp/lightning_webapp/data/fa_time_rolling')

    //
]

dataset_files_list = {
    TRACE: dataset_files_trace,
    LOVECLIM: dataset_files_loveclm,
    FAMOUS: dataset_files_famous,
}

def plot_lightning(request):
    if request.method == 'POST':
        lat_point = float(request.POST.get('latitude'))
        print(lat_point)
        lon_point = float(request.POST.get('longitude'))
        print(lat_point)
        dataset = request.POST.get('dataset')
        print(dataset)


        dataset_files = None

        if dataset == "ALL":
            plt.figure(figsize=(10, 6))
            for key, dataset_files in dataset_files_list.items():
                var = dataset_files[0]
                lat = dataset_files[1]
                lon = dataset_files[2]
                time = dataset_files[3]

                lat_idx = np.argmin(np.abs(lat - lat_point))
                lon_idx = np.argmin(np.abs(lon - lon_point))

                if lat_idx < 0 or lat_idx >= lat.shape[0] or lon_idx < 0 or lon_idx >= lon.shape[0]:
                    print(f"Error: Latitude or longitude values are out of bounds for the dataset {key}. Skipping.")
                    continue

                plt.plot(time, var[:, lat_idx, lon_idx], label=f'{key}')

            plt.xlabel('Time')
            plt.ylabel('Lightning')
            plt.title(f'All Datasets: Time series of Lightning at Lat: {lat_point}, Lon: {lon_point}')
            plt.grid(True)
            plt.legend()
            plt.tight_layout()
            plt.show()

            # Save the plot to a file
            plot_file_path = '/lightning-webapp/lightning_webapp/lightningapp/static/plots/plot.png'
            plt.savefig(plot_file_path)

            # Close the plot to prevent memory leaks
            plt.close()

            # Render the template with the plot
            template = loader.get_template('/lightning-webapp/lightning_webapp/lightningapp/templates/index.html')
            context = {'plot_file_path': plot_file_path}
            return HttpResponse(template.render(context, request))
        elif dataset in dataset_files_list:
            dataset_files = dataset_files_list[dataset]

            if -180 <= lat_point < 0:
                lat_point = lat_point + 360
            
            var = dataset_files[0]
            lat = dataset_files[1]
            lon = dataset_files[2]
            time = dataset_files[3]

            lat_idx = np.argmin(np.abs(lat - lat_point))
            lon_idx = np.argmin(np.abs(lon - lon_point))

            if lat_idx < 0 or lat_idx >= lat.shape[0] or lon_idx < 0 or lon_idx >= lon.shape[0]:
                print("Error: Latitude or longitude values are out of bounds for the dataset.")
                return

            plt.figure(figsize=(10, 6))
            plt.plot(time, var[:, lat_idx, lon_idx], marker='o')
            plt.xlabel('Time')
            plt.ylabel('Lightning')
            plt.title(f'{dataset}: Time series of Lightning at Lat: {lat_point}, Lon: {lon_point}')
            plt.grid(True)
            plt.tight_layout()
            plt.show()

            # Save the plot to a file
            plot_file_path = '/lightning-webapp/lightning_webapp/lightningapp/static/plots/plot.png'
            plt.savefig(plot_file_path)

            # Close the plot to prevent memory leaks
            plt.close()

            # Render the template with the plot
            template = loader.get_template('/lightning-webapp/lightning_webapp/lightningapp/templates/index.html')
            context = {'plot_file_path': plot_file_path}
            return HttpResponse(template.render(context, request))

        else:
            return HttpResponseBadRequest("Invalid dataset name")
        
    return HttpResponseBadRequest()
