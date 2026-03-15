import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    'age': [23,34,53,24,44,45,66,5,35,46,74,36,75,56]
})

his = px.histogram(
    df,
    x='age',
    title='Age distribution'
)
his.show()