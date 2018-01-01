"""
This module contains functions to get the safety of a country either from human attacks or natural diseasters
"""
import copy
import logging
import math
import re

from bs4 import BeautifulSoup, SoupStrainer
import requests

global_peace_index_url = "https://en.wikipedia.org/wiki/Global_Peace_Index"

status_from_color = {
    "Green": "Very safe", "YellowGreen": "Safe", "OrangeRed": "Slightly Dangerous",
    "Red": "Dangerous", "FireBrick": "Very Dangerous"
}

world_risk_url = "https://en.wikipedia.org/wiki/List_of_countries_by_natural_disaster_risk"


def safety_status_text(percent):
    """
    Gets status text using percent passed in
    :param percent: number to use to get text
        :type percent int
    :return:
        status: string describing status or None(if status text could not be determined
    """
    if percent in range(1, 19): status = "Very Safe"
    elif percent in range(19, 36): status = "Safe"
    elif percent in range(36, 53): status = "Slightly Safe"
    elif percent in range(53, 70): status = "Slightly Dangerous"
    elif percent in range(70, 87): status = "Dangerous"
    elif percent in range(87, 101): status = "Very Dangerous"
    else:
        logging.warning("Can not determine status of country")
        return None
    return status


def human_attack_safety_status(country, no_of_countries=163):
    """
    Get the safety of a country using the Global Peace Index(GPI).
    The GPI gauges global peace using three broad themes: the level of societal safety and security,the extent of
    ongoing domestic and international conflict and the degree of militarization
    :param country: Name of country to get status for
        :type country: str
    :param no_of_countries: Number of countries in current GPI ranking
        :type no_of_countries: int
    :return: Dict containing status for country or None(If status could not be determined)
    """
    response = requests.get(global_peace_index_url)
    website = BeautifulSoup(response.text, 'html.parser')
    table_rows = website.select("table tr")
    country_details = [rows for rows in table_rows if rows.find(title=re.compile(country)) is not None]\
                      or [rows for rows in table_rows if rows.find(title=re.compile(country.title())) is not None]
    if country_details:
        country_details_children = [child for child in country_details[0].children]
        country_latest_index = re.search(r"\d+", str(country_details_children[3])).group()
    else:
       logging.error("Can not find GPI details for this country {}".format(country))
       return None

    country_percentage = math.ceil((int(country_latest_index)/no_of_countries)*100)
    country_safety ={}
    country_safety['index']=country_latest_index
    country_safety['status'] = safety_status_text(country_percentage)
    return country_safety


def natural_disaster_safety_status(country):
    """
    Safety status of country from damage due to natural disasters(Earth quakes, floods , droughts etc) using World Risk Index
    :param country: Country to get safety status from
        :type country: str
    :return: Dict containing status for country or None(If status could not be determined)
    """
    res = requests.get(world_risk_url)
    website = BeautifulSoup(res.text, 'html.parser',parse_only=SoupStrainer('table'))
    country_a_element = website.find('a',text=country)
    if country_a_element:
        parent_td = country_a_element.find_parent('td')
        current_score_td  = parent_td.next_sibling.next_sibling
        if current_score_td.text:
            current_score_background = re.search(r'background:\w+',str(current_score_td)).group()
            current_score_color = current_score_background.lstrip('background:')
            return {'status_colour': current_score_color, 'status_text': status_from_color[current_score_color],
                    'index': parent_td.previous_sibling.previous_sibling.text}
        else:
            logging.error('Current world risk index data could not be determined for {}'.format(country))
            return None
    else:
        logging.error("Could not find natural disaster data for {country}".format(country=country))
        return None


def get_country_safety_stats(country):
    """
    Safety status of a country
    :param country: Country to get status of
        :type country str
    :return: Dict containing status of country or None
    """
    safety_stat = {}
    safety_stat['name'] = country
    safety_stat['natural_disaster_safety']  = natural_disaster_safety_status(country)
    safety_stat['human_attack_safety'] =  human_attack_safety_status(country)

    # to avoid run time error when looping
    for k,v in copy.deepcopy(safety_stat).items():
        if v is None:
            del safety_stat[k]
    return safety_stat

if __name__ == "__main__":
    print (human_attack_safety_status('Nigeria'))
    print(natural_disaster_safety_status('Palestine'))
    print(get_country_safety_stats('Nigeria'))
    print(get_country_safety_stats('Bosnia and Herzegovina'))
    print(get_country_safety_stats('Democratic Republic of the Congo'))
    print(get_country_safety_stats('Vanuatu'))
