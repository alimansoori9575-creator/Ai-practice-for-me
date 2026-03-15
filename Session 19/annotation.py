import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "epoch": range(1,11),
    "loss": [0.9,0.8,0.7,0.6,0.5,0.4,0.45,0.3,0.7,0.35]
})

Chart = px.line(
    df,
    x="epoch",
    y="loss",
    title= "Training loss over time with annotation"
)

Chart.add_annotation(
    x=5,
    y=0.5,
    text='Training mid point',#What txt u want to add
    showarrow=True,
    arrowhead=6# shape of arrow head
)
Chart.show()