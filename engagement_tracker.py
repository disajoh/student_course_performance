import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Load data
df = pd.read_csv('data/engagement_data.csv')

# data aggregation
engagement_summary = df.groupby('resource_type').agg(
    avg_time_spent=('time_spent', 'mean'),
    completion_rate=('completion', 'mean')
).reset_index()

# create Dash app
app = Dash(__name__)

###### CREATE CHARTs
# create bar chart
fig = px.bar(
    engagement_summary,
    x='resource_type',
    y='avg_time_spent',
    title='Average Time Spent by Resource Type',
    text='avg_time_spent'
)

# create line chart
fig2 = px.line(
    engagement_summary,
    x='resource_type',
    y='completion_rate',
    title='Completion Rate by Resource Type',
    markers=True
)

# layout
app.layout = html.Div([
    html.H1('Course Engagement Dashboard'),
    dcc.Graph(figure=fig),
    dcc.Graph(figure=fig2),
    html.Label('Filter by Metric'),
    dcc.Dropdown(
        id='metric-dropdown',
        options=[{'label': 'Time Spent', 'value': 'time'}, {'label': 'Completion Rate', 'value': 'rate'}],
        value='time'
    )
])


if __name__ == '__main__':
    app.run(port=8052, debug=True)
