# Data dashboard
### An excercise to deploy a web application with Python, Flask and Plotly

**Lars Tinnefeld**, 2020-12-24

![solar](https://images.unsplash.com/photo-1509391366360-2e959784a276?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1504&q=80)
Image: [American Public Power Association](https://unsplash.com/@publicpowerorg)

## Table of content
1. [Dashboard creation (Business understanding)](#business_understanding)
2. [Objectives](#objectives)
3. [Approach](#approach)
4. [Data](#data)
5. [Data preparation](#preparation)
6. [Data Modelling](#modelling)
7. [Evaluation](#evaluation)
8. [References and links](#references)

## Dashboard creation <a name="business_understanding"></a>
Dashboards are advanced ways to bring the results which are extracted from data to users. Good dashboards are interactive. Dashboards consist of two areas: The frontend with the visualizations and other information and the backend, where the data is wrangled and prepared for the visualization. There are many ways to create dashboards. In this example I used the light-weight web frame application Flask, Python for the data wrangling in the backend, HTML, CSS, Bootstrap for the web page itself and a bit of JavaScript to translate the data outcome into objects Pyplot can use to generate the charts.

## Objectives <a name="objectives"></a>
Even so the chosen data has an interesting content, the main focus in this repository is to develop the basic structure and functionality of a simple dashboard with can be deployed as web application.

## Approach <a name="approach"></a>
1) Simple web page with HTML, styled with Bootstrap and CSS stored in the template folder. At the beginning charts are just "dummy images".
2) Selecting data which can deliver an interesting story to show in the dashboard
3) Start with loading the data in a Jupyter Notebook, investigate content and perform exploratory data analysis.
4) Once the decision for the set of visualizations are made transfer the data-wrangling code which was used in the Jupyter Notebook into wrange_data.py
5) "routes.py" contains the code which translates the code and sets up the rendering procedure for the HTML page
6) The data is stored in the object "return_figures" and is available within the HTML file and can be accessed through JavaScript and Jinja syntax

## Data <a name="data"></a>
Text here...

## Data preparation <a name="preparation"></a>
Text here...

## Modelling <a name="modelling"></a>
Text here...

## Evaluation and conclusion <a name="evaluation"></a>
Text here...

## References and links <a name="references"></a>
Text here...
