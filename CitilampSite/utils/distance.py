"""
This module contains every thing that has to deal with distance
"""
import googlemaps

google_maps_key = "AIzaSyDBtjYL7sDcinwny6S0gHF8xC2uPwvcjEA"

gmaps = googlemaps.Client(key=google_maps_key)


def get_distance(origin, destination):
    """
    Get the distance from origin to destination

    :param origin: One location and/or latitude/longitude values,
        from which to calculate distance.
    :type origin: a single location

    :param destination: One address or lat/lng values, to
        which to calculate distance.
    :type destination: a single location

    :return: dict containing distance details
    """
    result = gmaps.distance_matrix(origin, destination)
    try:
        distance_details = result['rows'][0]['elements'][0]['distance']
    except KeyError:
        raise Exception("Could not get distance details, were origin and destination of the same type "
                        "ie where they both cities or countries")
    return distance_details


if __name__ == "__main__":
    print(get_distance('nigeria', 'germany'))
