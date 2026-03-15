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
    title= "Training loss over time"
)
Chart.show()