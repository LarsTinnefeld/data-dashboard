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
        title = 'Daily DC Power generation plant 1',
        xaxis = dict(
            title = 'Timeline',
            autoticks = False
            )
        )

    graph_two = []
    df_daily = daily_gen_grouping('data/Plant_2_Generation_Data.csv')
    x_val = df_daily['date']
    y_val = df_daily['DC_POWER']
    graph_two.append(
        go.Bar(
            x = x_val,
            y = y_val,
            #mode = 'lines',
            name = 'DC_POWER'
        )
    )
    layout_two = dict(
        title = 'Daily DC Power generation plant 2',
        xaxis = dict(
            title = 'Timeline',
            autoticks = False
            )
        )

    graph_three = []
    df = import_gen('data/Plant_1_Weather_Sensor_Data.csv')
    df_may_25 = df.loc[df.date == pd.to_datetime('2020-05-25')][['IRRADIATION', 'DATE_TIME']]
    x_val = df_may_25['DATE_TIME']
    y_val = df_may_25['IRRADIATION']
    graph_three.append(
        go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'markers',
            name = 'DC_POWER',
            marker=dict(
                color='LightSkyBlue',
                size=5,
                line=dict(
                    color='MediumPurple',
                    width=2
                    )
                )
            )
        )

    layout_three = dict(
        title = 'Irradiation for May 25, 2020',
        xaxis = dict(
            title = 'Timeline',
            autoticks = False
            )
        )

    graph_four = []
    df_x = daily_gen_grouping('data/Plant_1_Generation_Data.csv')
    df_y = daily_gen_grouping('data/Plant_2_Generation_Data.csv')
    df_xy = df_x.merge(df_y, on='date')

    labels = ['Plant 1', 'Plant 2']
    value_x = df_xy['DC_POWER_x'].sum()
    value_y = df_xy['DC_POWER_y'].sum()
    values = [value_x, value_y]

    graph_four.append(
        go.Pie(
            labels = labels,
            values = values,
            name = 'DC_POWER comparison',
            )
        )

    layout_four = dict(
        title = 'DC Power comparison'
        )

    figures = []
    figures.append(dict(data = graph_one, layout = layout_one))
    figures.append(dict(data = graph_two, layout = layout_two))
    figures.append(dict(data = graph_three, layout = layout_three))
    figures.append(dict(data = graph_four, layout = layout_four))

    return figures