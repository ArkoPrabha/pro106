import plotly.express as px
import csv
import numpy as np

def getdatasrc(data_path):
    y_axes=[]
    x_axes=[]
    with open(data_path)as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            y_axes.append(float(row['Marks In Percentage']))
            x_axes.append(float(row['Days Present']))
    return{'x':x_axes,'y':y_axes}

def findcorrelation(data_src):
    correlation=np.corrcoef(data_src['x'],data_src['y'])
    print('CORRELATION IS',correlation[0,1])

def setup():
    data_path='data.csv'
    data_src=getdatasrc(data_path)
    findcorrelation(data_src)

setup()