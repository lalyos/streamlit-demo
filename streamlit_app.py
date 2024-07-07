import streamlit as st
import folium

st.title("🎈 My new app")
st.write(
    "Let see a map ..."
)

folium.Map(location=(47, 18),zoom_start=12)
