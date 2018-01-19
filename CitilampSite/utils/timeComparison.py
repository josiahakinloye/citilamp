import arrow
import googlemaps


#todo change google map credentials

google_maps_key = "AIzaSyDBtjYL7sDcinwny6S0gHF8xC2uPwvcjEA"#"AIzaSyCHijPTy-zvupaNKEF3QqsnVDFpWBbw5gM "#"AIzaSyA60LdGkJ9Hz2LOnwjpOjDCk9m9gUxhM6s"#"AIzaSyCX35UUsEn5Q2duK_j674X-dSp-Xng5W_E"
gmaps = googlemaps.Client(key=google_maps_key)

def get_latitude_and_longitude(place):
    """
    Get the  latitude and longitude  of a place using the google maps api
    :param place: the place on earth to use eg: lagos, nigeria...
    :type place str
    :return: dict containing latitude_and_longitude of place
    """
    response = gmaps.geocode(place)
    try:
        latitude_and_longitude = response[0]['geometry']['location']
    except:
        raise Exception("Could not determine latitude and longitude")

    return latitude_and_longitude

def get_timedetails_of_location(place):
    """
    Get the current time at a place
    :param place: the name of place to get current time of
    :type place str
    :return: tuple containing  current date and time of place
    """
    details = {}
    latitude_and_longitude = get_latitude_and_longitude(place)
    try:
        print(gmaps.timezone(latitude_and_longitude))
        timezone_id = gmaps.timezone(latitude_and_longitude)['timeZoneId']
    except:
        raise Exception("Can not determine timezone of {place}".format(place=place))
    time_details = arrow.now(timezone_id).format('D/MMM/YY-h:mm A')
    date, time = time_details.split('-')

    details[place]=  (date, time)

    return details

def time_details_comparison(places):
    """
    Compare time details in places
    :param places: iter of strings where each string is a place
    :type places list, dict or tuple containing list of place to do comparison for
    :return: list of comparison details
    """
    comparison_list = []
    for place in places:
        comparison_list.append(get_timedetails_of_location(place))
    return comparison_list

if __name__ == "__main__":
    print(time_details_comparison(['lagos', 'germany', 'white house']))
