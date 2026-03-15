import pandas as pd
import plotly.express as px
import numpy as np

df = pd.DataFrame({
    "x": np.random.randn(1000),
    "y": np.random.randn(1000),
    'group': np.random.choice(['A','B','C','D'], 1000)
})

Chart = px.line(
    df,
    x="x",
    y="y",
    title= "Cluster visualisation",
    color='group',
    color_discrete_sequence=['#ff28e6', "#3700fe","#ff0336", "#ffff00"]
)

# to eport we have installed kaleido 
Chart.write_image('plot.png')
#Chart.write_image('plot.jpg')
#Chart.write_image('plot.svg')
#Chart.write_image('plot.webp')
#Chart.write_image('plot.pdf')