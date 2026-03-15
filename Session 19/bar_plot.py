import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "model": ['Model A','Model B','Model C'],
    "accuracy": [16,10,31]
})

Chart = px.bar(
    df,
    x="model",
    y="accuracy",
    title= "Model accuracy comparison"
)
Chart.show()