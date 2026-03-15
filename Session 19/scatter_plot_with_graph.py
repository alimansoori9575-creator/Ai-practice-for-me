import pandas as pd
import plotly.express as px
import numpy as np

df = pd.DataFrame({
    "x": np.random.randn(1000),
    "y": np.random.randn(1000),
    'group': np.random.choice(['A','B','C','D'], 1000)
})

Chart = px.scatter(
    df,
    x="x",
    y="y",
    title= "Cluster visualisation",
    color='group',
    color_discrete_sequence=['#ff28e6', "#3700fe","#ff0336", "#ffff00"]
)
Chart.show()