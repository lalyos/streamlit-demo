import folium
import streamlit as st
from streamlit_folium import st_folium
import gpxpy
import gpxpy.gpx
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

st.title("🎈 Sztrava")
st.write(
    "Let see a map ..."
)



def parse_gpx(file_path):
    with open(file_path, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    points = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                points.append((point.latitude, point.longitude, point.time))

    return points

def calculate_speeds(points):
    speeds = []
    for i in range(1, len(points)):
        lat1, lon1, time1 = points[i-1]
        lat2, lon2, time2 = points[i]

        time_diff = (time2 - time1).total_seconds() / 3600.0  # Time difference in hours
        dist = np.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2) * 111  # Distance in km (approx)
        speed = dist / time_diff if time_diff > 0 else 0
        speeds.append(speed)

    return speeds

def speed_to_color(speed, min_speed=0, max_speed=30):
    """Interpolate color between red and green based on speed."""
    speed = max(min_speed, min(speed, max_speed))  # Clamp speed to [min_speed, max_speed]
    ratio = (speed - min_speed) / (max_speed - min_speed)  # Scale to [0, 1]
    red = int(255 * (1 - ratio))
    green = int(255 * ratio)
    blue = 0
    return f'#{red:02x}{green:02x}{blue:02x}'

def create_map(points, speeds):
    m = folium.Map(location=[points[0][0], points[0][1]], zoom_start=13)

    for i in range(1, len(points)):
        lat1, lon1, _ = points[i-1]
        lat2, lon2, _ = points[i]
        color = speed_to_color(speeds[i-1])
        folium.PolyLine(
            locations=[(lat1, lon1), (lat2, lon2)],
            color=color,
            weight=5,
            opacity=0.7
        ).add_to(m)

    return m



name = 'dw-07-04'
# file_path = '/content/drive/MyDrive/downwind/' + name + '.gpx'
file_path = name + '.gpx'

points = parse_gpx(file_path)
speeds = calculate_speeds(points)
m = create_map(points, speeds)

# m = folium.Map(location=(47, 18),zoom_start=12)



# call to render Folium map in Streamlit, but don't get any data back
# from the map (so that it won't rerun the app when the user interacts)
st_folium(m, width=725, returned_objects=[])