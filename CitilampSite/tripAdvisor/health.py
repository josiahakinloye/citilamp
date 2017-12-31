"""
This module contains health related advice eg diseases to watch out for
"""

from bs4 import BeautifulSoup, SoupStrainer
import logging
import re
import requests

travel_tips_url = "https://wwwnc.cdc.gov"
travel_tips_url_to_query = travel_tips_url+"/travel/destinations/traveler/none/{country}?s_cid=ncezid-dgmq-travel-single-001"

country_dict = {'Easter Island': 'easter-island', 'Puerto Rico': 'puerto-rico', 'Costa Rica': 'costa-rica', 'Libya': 'libya', 'Rwanda': 'rwanda', 'Jersey': 'united-kingdom', 'Colombia': 'colombia', 'Saint Barthelemy': 'saint-barthelemy', 'Antarctica': 'antarctica', 'Rota': 'northern-mariana-islands', 'Suriname': 'suriname', 'Romania': 'romania', 'Belgium': 'belgium', 'Cook Islands': 'cook-islands', 'Austral Islands': 'french-polynesia', 'Yemen': 'yemen', 'Pakistan': 'pakistan', 'Wake Island': 'wake-island', 'Virgin Islands, U.S.': 'usvirgin-islands', 'Dominican Republic': 'dominican-republic', 'Malaysia': 'malaysia', "Côte d'Ivoire": 'ivory-coast', 'Micronesia, Federated States of': 'micronesia', 'Tinian': 'northern-mariana-islands', 'Seychelles': 'seychelles', 'Sweden': 'sweden', 'Argentina': 'argentina', 'Saint Thomas': 'usvirgin-islands', 'Saint Lucia': 'saint-lucia', 'Japan': 'japan', 'Vanuatu': 'vanuatu', 'South Korea': 'south-korea', 'Djibouti': 'djibouti', 'South Georgia and the South Sandwich Islands': 'south-georgia-south-sandwich-islands', 'Azores': 'azores', 'Norway': 'norway', 'Saint Martin': 'saint-martin', 'United Arab Emirates': 'united-arab-emirates', 'Monaco': 'monaco', 'Palau': 'palau', 'China': 'china', 'Moldova': 'moldova', 'Somalia': 'somalia', 'Saint Croix': 'usvirgin-islands', 'Sint Maarten': 'sint-maarten', 'Ethiopia': 'ethiopia', 'Greece': 'greece', 'Curaçao': 'curacao', 'Poland': 'poland', 'Algeria': 'algeria', 'Lebanon': 'lebanon', 'Madagascar': 'madagascar', 'Equatorial Guinea': 'equatorial-guinea', 'Sierra Leone': 'sierra-leone', 'Bora-Bora': 'french-polynesia', 'England': 'united-kingdom', 'Holy See': 'italy', 'Oman': 'oman', 'Czech Republic': 'czech-republic', 'Caicos Islands': 'turks-and-caicos', 'Republic of the Congo': 'congo', 'Aruba': 'aruba', 'Uganda': 'uganda', 'Singapore': 'singapore', 'Benin': 'benin', 'Lithuania': 'lithuania', 'Slovakia': 'slovakia', 'Latvia': 'latvia', 'The Gambia': 'the-gambia', 'Montenegro': 'montenegro', 'Netherlands, The': 'netherlands', 'Sudan': 'sudan', 'Macau SAR': 'macau-sar', 'Faroe Islands': 'faroe-island', 'Antigua and Barbuda': 'antigua-and-barbuda', 'Brazil': 'brazil', 'Martinique': 'martinique', 'Guadeloupe': 'guadeloupe', 'Barbados': 'barbados', 'Jost Van Dyke': 'british-virgin-islands', 'Syria': 'syria', 'Tajikistan': 'tajikistan', 'Senegal': 'senegal', 'Mauritania': 'mauritania', 'Kosovo': 'kosovo', 'South Sudan': 'south-sudan', 'Burma': 'burma', 'Angola': 'angola', 'Bermuda': 'bermuda', 'Liechtenstein': 'liechtenstein', 'Virgin Gorda': 'british-virgin-islands', 'Dubai': 'united-arab-emirates', 'Falkland Islands': 'falkland-islands', 'Cuba': 'cuba', 'Zimbabwe': 'zimbabwe', 'Iran': 'iran', 'Tanzania': 'tanzania', 'New Zealand': 'new-zealand', 'Timor-Leste': 'east-timor', 'Sri Lanka': 'sri-lanka', 'Nepal': 'nepal', 'Belize': 'belize', 'Central African Republic': 'central-african-republic', 'Guinea-Bissau': 'guinea-bissau', 'Kiribati': 'kiribati', 'United Kingdom': 'united-kingdom', 'Bosnia and Herzegovina': 'bosnia-and-herzegovina', 'Saudi Arabia': 'saudi-arabia', 'Democratic Republic of the Congo': 'democratic-republic-of-congo', 'Nauru': 'nauru', 'Liberia': 'liberia', 'Chile': 'chile', 'Armenia': 'armenia', 'Anegada': 'british-virgin-islands', 'Botswana': 'botswana', 'Niger': 'niger', 'Marquesas Islands': 'french-polynesia', 'Switzerland': 'switzerland', 'Dominica': 'dominica', 'Moorea': 'french-polynesia', 'Burkina Faso': 'burkina-faso', 'Kyrgyzstan': 'kyrgyzstan', 'San Marino': 'san-marino', 'Mexico': 'mexico', 'Gibraltar': 'gibraltar', 'Finland': 'finland', 'El Salvador': 'el-salvador', 'Lesotho': 'lesotho', 'Panama': 'panama', 'French Guiana': 'french-guiana', 'Malta': 'malta', 'South Sandwich Islands': 'south-georgia-south-sandwich-islands', 'Iceland': 'iceland', 'Saint Helena': 'saint-helena', 'Georgia': 'georgia', 'Hungary': 'hungary', 'Tortola': 'british-virgin-islands', 'Macedonia': 'macedonia', 'Bonaire': 'bonaire', 'United States': 'united-states', 'Denmark': 'denmark', 'Saba': 'saba', 'Saint John': 'usvirgin-islands', 'Galápagos Islands': 'ecuador', 'Grenada': 'grenada', 'New Caledonia': 'new-caledonia', 'Comoros': 'comoros', 'Cayman Islands': 'cayman-islands', 'Society Islands': 'french-polynesia', 'Uruguay': 'uruguay', 'Canary Islands': 'canary-islands', 'Chad': 'chad', 'Luxembourg': 'luxembourg', 'Eritrea': 'eritrea', 'Scotland': 'united-kingdom', 'Guatemala': 'guatemala', 'Marshall Islands': 'marshall-islands', 'Jamaica': 'jamaica', 'Trinidad and Tobago': 'trinidad-and-tobago', 'Saint Kitts and Nevis': 'st-kitts-and-nevis', 'Barbuda': 'antigua-and-barbuda', 'Thailand': 'thailand', 'Maldives': 'maldives', 'Christmas Island': 'christmas-island', 'Andorra': 'andorra', 'Mauritius': 'mauritius', 'Solomon Islands': 'solomon-islands', 'Azerbaijan': 'azerbaijan', 'Philippines': 'philippines', 'Spain': 'spain', 'Bhutan': 'bhutan', 'Turks and Caicos Islands': 'turks-and-caicos', 'Estonia': 'estonia', 'Sint Eustatius': 'sint-eustatius', 'Bahamas, The': 'the-bahamas', 'Serbia': 'serbia', 'Pitcairn Islands': 'pitcairn-islands', 'Anguilla': 'anguilla', 'Western Sahara': 'western-sahara', 'Gabon': 'gabon', 'Cocos Islands': 'cocos-islands', 'South Africa': 'south-africa', 'Guyana': 'guyana', 'Hong Kong SAR': 'hong-kong-sar', 'Canada': 'canada', 'Tubuai': 'french-polynesia', 'Qatar': 'qatar', 'Nigeria': 'nigeria', 'Ivory Coast': 'ivory-coast', 'Guam': 'guam', 'Fiji': 'fiji', 'Nicaragua': 'nicaragua', 'Guinea': 'guinea', 'Kuwait': 'kuwait', 'British Indian Ocean Territory': 'british-indian-ocean-territory', 'France': 'france', 'Austria': 'austria', 'Kazakhstan': 'kazakhstan', 'Morocco': 'morocco', 'Haiti': 'haiti', 'Tuvalu': 'tuvalu', 'Laos': 'laos', 'Northern Mariana Islands': 'northern-mariana-islands', 'Swaziland': 'swaziland', 'Italy': 'italy', 'Bolivia': 'bolivia', 'Australia': 'australia', 'Albania': 'albania', 'Vietnam': 'vietnam', 'Croatia': 'croatia', 'Papua New Guinea': 'papua-new-guinea', 'Belarus': 'belarus', 'Bangladesh': 'bangladesh', 'Rurutu': 'french-polynesia', 'Togo': 'togo', 'Paraguay': 'paraguay', 'Taiwan': 'taiwan', 'Isle of Man': 'united-kingdom', 'India': 'india', 'Jordan': 'jordan', 'Uzbekistan': 'uzbekistan', 'Tobago': 'trinidad-and-tobago', 'French Polynesia': 'french-polynesia', 'Madeira Islands': 'maderia-islands', 'São Tomé and Príncipe': 'sao-tome-and-principe', 'Portugal': 'portugal', 'Mozambique': 'mozambique', 'Turkey': 'turkey', 'Namibia': 'namibia', 'Russia': 'russia', 'Kenya': 'kenya', 'Israel': 'israel', 'Ecuador': 'ecuador', 'Mongolia': 'mongolia', 'Northern Ireland': 'united-kingdom', 'North Korea': 'north-korea', 'Ghana': 'ghana', 'Cape Verde': 'cape-verde', 'Peru': 'peru', 'Cyprus': 'cyprus', 'Ireland': 'ireland', 'American Samoa': 'american-samoa', 'Niue': 'niue', 'Mayotte': 'mayotte', 'Wales': 'united-kingdom', 'Afghanistan': 'afghanistan', 'Bulgaria': 'bulgaria', 'Honduras': 'honduras', 'Cameroon': 'cameroon', 'Turkmenistan': 'turkmenistan', 'Guernsey': 'united-kingdom', 'Réunion': 'reunion', 'Slovenia': 'slovenia', 'Egypt': 'egypt', 'Burundi': 'burundi', 'Myanmar': 'burma', 'Mali': 'mali', 'Malawi': 'malawi', 'Samoa': 'samoa', 'Virgin Islands, British ': 'british-virgin-islands', 'Greenland': 'greenland', 'Tunisia': 'tunisia', 'Tokelau': 'tokelau', 'Ukraine': 'ukraine', 'Venezuela': 'venezuela', 'Grenadines': 'saint-vincent-and-the-grenadines', 'Zambia': 'zambia', 'Zanzibar': 'tanzania', 'Vatican City': 'italy', 'Germany': 'germany', 'Montserrat': 'montserrat', 'Bahrain': 'bahrain', 'Tahiti': 'french-polynesia', 'Saint Pierre and Miquelon': 'saint-pierre-and-miquelon', 'Indonesia': 'indonesia', 'Tonga': 'tonga', 'Cambodia': 'cambodia', 'Norfolk Island': 'norfolk-island', 'Saipan': 'northern-mariana-islands', 'Iraq': 'iraq', 'Saint Vincent and the Grenadines': 'saint-vincent-and-the-grenadines', 'Brunei': 'brunei'}


def traveler_advice(css_class):
    return css_class == "traveler-disease" or css_class == "traveler-findoutwhy"

def traveler_info(res):
    website_data = BeautifulSoup(res.text, "html.parser", parse_only=SoupStrainer(class_=traveler_advice))

    website_data_p = [didts(child) for child in website_data.find_all(class_="traveler-disease")]

    website_data_kl = [child.text for child in website_data.find_all(class_="traveler-findoutwhy"
)]

    return list(zip (website_data_p, website_data_kl))

def child(l):
    new_diect = {}
    new_diect[l[0][0]] = {'link':travel_tips_url+l[0][1],'info':l[1]}
    return new_diect

def get_health_for_countries(country):
    try:
        country_query_string = country_dict[country]
    except KeyError:
        logging.error("Ensure country was passed in this format Nigeria or or Turks and Caicos Islands Saint Vincent and the Grenadines")
        return False
    res = requests.get(travel_tips_url_to_query.format(country=country_query_string))
    lk = list( traveler_info(res))

    return  [child(you) for you in lk]
def didts(child):
    disease = child.find('a')
    if disease:
        return  disease.text, disease.get('href')

if __name__ == "__main__":
    print (get_health_for_countries('Denmark'))
