import csv
import plotly.express as px
import pandas as pd
with open('data.csv')as f:
    """ df=csv.DictReader(f)
    print(df) """
    df1=pd.read_csv(f)
    #print(df1)
    fig=px.scatter(df1,x='Days Present',y='Marks In Percentage')
    fig.show()