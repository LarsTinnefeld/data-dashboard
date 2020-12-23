# Importing libraries
import pandas as pd
import datetime as dt
import plotly.graph_objs as go

# Data import procedure

def import_gen(dataset):
    
    df = pd.read_csv(dataset) # Import data
    df['DATE_TIME'] = pd.to_datetime(df['DATE_TIME']) # Set date format
    df['date'] = df['DATE_TIME'].dt.date # Add date column

    return df


def daily_gen_grouping(dataset):

    df = import_gen(dataset)
    df_daily = df.groupby('date').agg({'DC_POWER': 'sum', 'AC_POWER': 'sum', 'DAILY_YIELD': 'max'}).reset_index()

    return df_daily


def return_figures():

    graph_one = []
    df_daily = daily_gen_grouping('data/Plant_1_Generation_Data.csv')

    x_val = df_daily['date']
    y_val = df_daily['DC_POWER']

    graph_one.append(
        go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'lines',
            name = 'DC_POWER'
        )
    )

    layout_one = dict(
        title = 'Daily summarized DC Power generation',
        xaxis = dict(
            title = 'Timeline',
            autoticks = False
            )
        )

    figures = []
    figures.append(dict(data = graph_one, layout = layout_one))

    return figures