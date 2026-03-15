import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "users": [100,150,200,500,1000],
    "purchase": [20,30,23,60,110]
})

Chart = px.scatter(
    df,
    x="users",
    y="purchase",
    title= "Users vs Purchases relationship"
)
Chart.show()