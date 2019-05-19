import pandas as pd
import os


def csv_to_pandas(file_name, delimiter):
    return pd.read_csv(f'static/tables/{file_name}', sep=delimiter)


def get_plot_filenames():
    plot_file_dict = {'bachelor': {'bar_plots': os.listdir('static/images/bachelor/bar_plots'),
                                   'line_plots': os.listdir('static/images/bachelor/line_plots')},
                      'master': {'bar_plots': os.listdir('static/images/master/bar_plots'),
                                 'line_plots': os.listdir('static/images/master/line_plots')}
                      }
    return plot_file_dict
