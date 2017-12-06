"""
This module contains everything that has to do with weather
"""

from apixu.client import ApixuClient #weather api
import arrow #for time manipulation

weather_api_key = '89189bbae09641d89b3181117172511'

weather_client = ApixuClient(weather_api_key)

def get_weather_forecast_comparison(user_city="lagos", explored_city="london", days=7):
    """
    Compares the weather forecast of two cities passed in
    :param user_city: String The city the author in browsing from , this is to be obtained on the front end with the Html
    :param explored_city: String The city the author is exploring ie the city the author is viewing on the website
    :param days: Int Number of days you want to compare weather forecast for
    :return: Zip object containing info of weather comparision
    """
    user_city_forecast = weather_client.getForecastWeather(q=user_city, days=days)['forecast']['forecastday']
    explored_city_forecast = weather_client.getForecastWeather(q=explored_city, days=days)['forecast']['forecastday']
    weather_forecast_comparison = zip(map(return_stuff, user_city_forecast), map(return_stuff, explored_city_forecast))
    return weather_forecast_comparison



def return_stuff(forecast):
    """
    This returns a dictionary of relevant weather info
    :param forecast: List of weather info for a particular day
    :return: Dict of  relevant info to be displayed
    """
    day_forecast = {}
    day_forecast['condition_text'] = forecast['day']['condition']['text']
    day_forecast['condition_icon'] = forecast['day']['condition']['icon']
    day_forecast['max_temp'] = forecast['day']['maxtemp_c']
    day_forecast['min_temp'] = forecast['day']['mintemp_c']
    day_forecast['avg_temp'] = forecast['day']['avgtemp_c']
    day_info = arrow.get(forecast['hour'][0]['time']).format('MMM-DD:dddd').split(':')
    day_forecast['day'] = day_info[0]
    day_forecast['weekday'] = day_info[1]
    return day_forecast


if __name__ == "__main__":
    weather_comparison = get_weather_forecast_comparison()
    for comparison in weather_comparison:
        print (comparison)
