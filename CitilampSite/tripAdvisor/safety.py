"""
This module contains functions to get the safetu of a country either from humman attacks or natural diseasters
"""
import math
import re

from bs4 import BeautifulSoup, SoupStrainer
import requests

global_peace_index_url = "https://en.wikipedia.org/wiki/Global_Peace_Index"

def get_safety_status(percent):
    percent_to_use = int(percent)
    if percent_to_use in range(1,19) : status = "Very Safe"
    elif percent_to_use in range(19,36) : status = "Safe"
    elif percent_to_use in range(36,53) : status = "Slightly Safe"
    elif percent_to_use in range(53,70) : status = "Slightly Dangerous"
    elif percent_to_use in range(70,87): status = "Dangerous"
    elif percent_to_use in range(87,101) : status = "Very Dangerous"
    else:
        raise Exception("Can not determine status of country")
    return status

def get_safety_index(country, no_of_countries=163):
    response = requests.get(global_peace_index_url)
    website = BeautifulSoup(response.text, 'html.parser')
    table_rows = website.select("table tr")
    country_details = [rows for rows in table_rows if rows.find(title=re.compile(country)) is not None]\
                      or [rows for rows in table_rows if rows.find(title=re.compile(country.title())) is not None]
    if country_details:
        # pick only the number
        country_latest_index = re.search(r"\d+",[child for child in country_details[0].children][3].string).group()
    else:
        raise Exception("Can not find details for this country {}".format(country))

    country_percentage = math.ceil((int(country_latest_index)/no_of_countries)*100)
    country_safety ={}
    country_safety['index']=country_latest_index
    country_safety['status'] = get_safety_status(country_percentage)
    return country_safety


natural_dieaseter = "https://en.wikipedia.org/wiki/List_of_countries_by_natural_disaster_risk"
def get_natural(country):
    res = requests.get(natural_dieaseter)
    website = BeautifulSoup(res.text, 'html.parser',parse_only=SoupStrainer('table'))
    website2 = website.find('a',title=country)
    th  = website2.find_parent('td')
    return website2.text, th.next_sibling.next_sibling


if __name__ == "__main__":
    """
    print (get_safety_index('Republic of the Congo'))
    print(get_safety_index('nigeria'))
    """
    print(get_natural('Nigeria'))
