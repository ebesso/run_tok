import math


def bounding_box(lat, lon, dist_km):
    km_per_deg_lat = 111.32

    half_side_km = dist_km / 2.0
    
    delta_lat = half_side_km / km_per_deg_lat
    delta_lon = half_side_km / (km_per_deg_lat * math.cos(math.radians(lat)))
    
    nw = (lat + delta_lat, lon - delta_lon)
    ne = (lat + delta_lat, lon + delta_lon)
    sw = (lat - delta_lat, lon - delta_lon)
    se = (lat - delta_lat, lon + delta_lon)

    max_lat = lat + delta_lat
    min_lat = lat - delta_lat
    max_lon = lon + delta_lon
    min_lon = lon - delta_lon

    return {"nw": nw, "ne": ne, "sw": sw, "se": se, "min_lat": min_lat, "max_lat": max_lat, "min_lon": min_lon, "max_lon": max_lon}