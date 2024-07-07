import folium
import streamlit as st
from streamlit_folium import st_folium



st.title("🎈 Sztrava")
st.write(
    "Let see a map ..."
)

# m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)

m = folium.Map(location=(47, 18),zoom_start=12)


# folium.Marker(
#     [39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell"
# ).add_to(m)


# call to render Folium map in Streamlit, but don't get any data back
# from the map (so that it won't rerun the app when the user interacts)
st_folium(m, width=725, returned_objects=[])