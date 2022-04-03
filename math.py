import pandas as pd
import plotly.graph_objects as pg
import plotly.express as px
import csv

df = pd.read_csv("StudentData.csv")
studentDf = df.loc[df['student_id']=="TRL_987"]
print(studentDf.groupby("level")["attempt"].mean())

fig = px.scatter(df, x="student_id", y="level",size="attempt")
fig.show()