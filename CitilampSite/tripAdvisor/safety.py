"""
This module contains functions to get the safetu of a country either from humman attacks or natural diseasters
"""
import copy
import logging
import math
import re

from bs4 import BeautifulSoup, SoupStrainer
import requests

global_peace_index_url = "https://en.wikipedia.org/wiki/Global_Peace_Index"

status_from_color = {
    "Green": "Very safe", "YellowGreen" : "Safe", "OrangeRed" : "Slightly Dangerous",
    "Red" : "Dangerous", "FireBrick" : "Very Dangerous"
}

world_risk_url = "https://en.wikipedia.org/wiki/List_of_countries_by_natural_disaster_risk"

def get_safety_status(percent):
    percent_to_use = int(percent)
    if percent_to_use in range(1,19) : status = "Very Safe"
    elif percent_to_use in range(19,36) : status = "Safe"
    elif percent_to_use in range(36,53) : status = "Slightly Safe"
    elif percent_to_use in range(53,70) : status = "Slightly Dangerous"
    elif percent_to_use in range(70,87): status = "Dangerous"
    elif percent_to_use in range(87,101) : status = "Very Dangerous"
    else:
        logging.warning("Can not determine status of country")
        return None
    return status

def get_safety_index(country, no_of_countries=163):
    response = requests.get(global_peace_index_url)
    website = BeautifulSoup(response.text, 'html.parser')
    table_rows = website.select("table tr")
    country_details = [rows for rows in table_rows if rows.find(title=re.compile(country)) is not None]\
                      or [rows for rows in table_rows if rows.find(title=re.compile(country.title())) is not None]
    if country_details:
        country_latest_index = re.search(r"\d+",[child for child in country_details[0].children][3].string).group()
    else:
       logging.warning("Can not find details for this country {}".format(country))
       return None

    country_percentage = math.ceil((int(country_latest_index)/no_of_countries)*100)
    country_safety ={}
    country_safety['index']=country_latest_index
    country_safety['status'] = get_safety_status(country_percentage)
    return country_safety


#todo how to handle requests errors
def get_natural(country):
    res = requests.get(world_risk_url)
    website = BeautifulSoup(res.text, 'html.parser',parse_only=SoupStrainer('table'))
    website2 = website.find('a',text=country)
    if website2:
        parent_td = website2.find_parent('td')
        th  = parent_td.next_sibling.next_sibling
        if th.text:
            kl = re.search(r'background:\w+',str(th)).group().lstrip('background:')
            return {'index':status_from_color[kl], 'status':parent_td.previous_sibling.previous_sibling.text}
        else:
            logging.error('Current world risk index data could not be determined for {}'.format(country))
            return None
    else:
        logging.error("Could not find natural disaster data for {country}".format(country=country))
        return None


def getStat(country):
    stat = {}
    stat['name'] = country
    stat['natural']  = get_natural(country)
    stat['human'] =  get_safety_index(country)
    for k,v in copy.deepcopy(stat).items():
        if v is None:
            del stat[k]
    return stat

if __name__ == "__main__":
    #print(get_safety_index('Nigeria'))
    #print(get_natural('Palestine'))
    #print(getStat('Nigeria'))
    #print(getStat('Bosnia and Herzegovina'))
    print(getStat('Democratic Republic of the Congo'))
    print(getStat('Vanuatu'))