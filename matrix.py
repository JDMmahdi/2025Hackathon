import plotly.graph_objects as go
import streamlit as st
fig = go.Figure(data=[go.Mesh3d(
    x=[-1.5, 1, 1, -4],
    y=[-1, -1, 1, 9],
    z=[-1, -1, -1, -2],
    color='rgba(255, 0, 0, 0.6)',
    opacity=0.5
)])
fig = go.Figure(data=[go.Mesh3d(
    x=[-1.5, 1, 1, -3],
    y=[10, -1, 4, 1],
    z=[-1, 9, -4, -7],
    color='rgba(255, 0, 0, 0.6)',
    opacity=0.5
)])
fig.update_layout(scene=dict(
    xaxis=dict(range=[-10, 10]),
    yaxis=dict(range=[-10, 10]),
    zaxis=dict(range=[-10, 10])
))
st.plotly_chart(fig)