import math

def bounding_box(lat, lon, dist_km):
    """
    Returns the bounding box (min_lat, min_lon, max_lat, max_lon) around a point
    with side lengths of dist_km (in kilometers).
    """
    # Earth's radius in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)

    # Half side in km
    half_side = dist_km / 2.0

    # Latitude: 1 deg = 110.574 km
    delta_lat = half_side / 110.574

    # Longitude: 1 deg = 111.320*cos(latitude) km
    delta_lon = half_side / (111.320 * math.cos(lat_rad))

    min_lat = lat - delta_lat
    max_lat = lat + delta_lat
    min_lon = lon - delta_lon
    max_lon = lon + delta_lon

    return (min_lat, min_lon, max_lat, max_lon)