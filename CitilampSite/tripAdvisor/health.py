"""
This module contains health related advice eg diseases to watch out for
"""

from bs4 import BeautifulSoup, SoupStrainer
import logging
import requests

base_health_tips_url = "https://wwwnc.cdc.gov"
travel_tips_url_to_query = base_health_tips_url + "/travel/destinations/traveler/none/{country}?s_cid=ncezid-dgmq-travel-single-001"

# dictionary used to get query parameter used to get country_query_string
country_dict = {'Easter Island': 'easter-island', 'Puerto Rico': 'puerto-rico', 'Costa Rica': 'costa-rica', 'Libya': 'libya', 'Rwanda': 'rwanda', 'Jersey': 'united-kingdom', 'Colombia': 'colombia', 'Saint Barthelemy': 'saint-barthelemy', 'Antarctica': 'antarctica', 'Rota': 'northern-mariana-islands', 'Suriname': 'suriname', 'Romania': 'romania', 'Belgium': 'belgium', 'Cook Islands': 'cook-islands', 'Austral Islands': 'french-polynesia', 'Yemen': 'yemen', 'Pakistan': 'pakistan', 'Wake Island': 'wake-island', 'Virgin Islands, U.S.': 'usvirgin-islands', 'Dominican Republic': 'dominican-republic', 'Malaysia': 'malaysia', "Côte d'Ivoire": 'ivory-coast', 'Micronesia, Federated States of': 'micronesia', 'Tinian': 'northern-mariana-islands', 'Seychelles': 'seychelles', 'Sweden': 'sweden', 'Argentina': 'argentina', 'Saint Thomas': 'usvirgin-islands', 'Saint Lucia': 'saint-lucia', 'Japan': 'japan', 'Vanuatu': 'vanuatu', 'South Korea': 'south-korea', 'Djibouti': 'djibouti', 'South Georgia and the South Sandwich Islands': 'south-georgia-south-sandwich-islands', 'Azores': 'azores', 'Norway': 'norway', 'Saint Martin': 'saint-martin', 'United Arab Emirates': 'united-arab-emirates', 'Monaco': 'monaco', 'Palau': 'palau', 'China': 'china', 'Moldova': 'moldova', 'Somalia': 'somalia', 'Saint Croix': 'usvirgin-islands', 'Sint Maarten': 'sint-maarten', 'Ethiopia': 'ethiopia', 'Greece': 'greece', 'Curaçao': 'curacao', 'Poland': 'poland', 'Algeria': 'algeria', 'Lebanon': 'lebanon', 'Madagascar': 'madagascar', 'Equatorial Guinea': 'equatorial-guinea', 'Sierra Leone': 'sierra-leone', 'Bora-Bora': 'french-polynesia', 'England': 'united-kingdom', 'Holy See': 'italy', 'Oman': 'oman', 'Czech Republic': 'czech-republic', 'Caicos Islands': 'turks-and-caicos', 'Republic of the Congo': 'congo', 'Aruba': 'aruba', 'Uganda': 'uganda', 'Singapore': 'singapore', 'Benin': 'benin', 'Lithuania': 'lithuania', 'Slovakia': 'slovakia', 'Latvia': 'latvia', 'The Gambia': 'the-gambia', 'Montenegro': 'montenegro', 'Netherlands, The': 'netherlands', 'Sudan': 'sudan', 'Macau SAR': 'macau-sar', 'Faroe Islands': 'faroe-island', 'Antigua and Barbuda': 'antigua-and-barbuda', 'Brazil': 'brazil', 'Martinique': 'martinique', 'Guadeloupe': 'guadeloupe', 'Barbados': 'barbados', 'Jost Van Dyke': 'british-virgin-islands', 'Syria': 'syria', 'Tajikistan': 'tajikistan', 'Senegal': 'senegal', 'Mauritania': 'mauritania', 'Kosovo': 'kosovo', 'South Sudan': 'south-sudan', 'Burma': 'burma', 'Angola': 'angola', 'Bermuda': 'bermuda', 'Liechtenstein': 'liechtenstein', 'Virgin Gorda': 'british-virgin-islands', 'Dubai': 'united-arab-emirates', 'Falkland Islands': 'falkland-islands', 'Cuba': 'cuba', 'Zimbabwe': 'zimbabwe', 'Iran': 'iran', 'Tanzania': 'tanzania', 'New Zealand': 'new-zealand', 'Timor-Leste': 'east-timor', 'Sri Lanka': 'sri-lanka', 'Nepal': 'nepal', 'Belize': 'belize', 'Central African Republic': 'central-african-republic', 'Guinea-Bissau': 'guinea-bissau', 'Kiribati': 'kiribati', 'United Kingdom': 'united-kingdom', 'Bosnia and Herzegovina': 'bosnia-and-herzegovina', 'Saudi Arabia': 'saudi-arabia', 'Democratic Republic of the Congo': 'democratic-republic-of-congo', 'Nauru': 'nauru', 'Liberia': 'liberia', 'Chile': 'chile', 'Armenia': 'armenia', 'Anegada': 'british-virgin-islands', 'Botswana': 'botswana', 'Niger': 'niger', 'Marquesas Islands': 'french-polynesia', 'Switzerland': 'switzerland', 'Dominica': 'dominica', 'Moorea': 'french-polynesia', 'Burkina Faso': 'burkina-faso', 'Kyrgyzstan': 'kyrgyzstan', 'San Marino': 'san-marino', 'Mexico': 'mexico', 'Gibraltar': 'gibraltar', 'Finland': 'finland', 'El Salvador': 'el-salvador', 'Lesotho': 'lesotho', 'Panama': 'panama', 'French Guiana': 'french-guiana', 'Malta': 'malta', 'South Sandwich Islands': 'south-georgia-south-sandwich-islands', 'Iceland': 'iceland', 'Saint Helena': 'saint-helena', 'Georgia': 'georgia', 'Hungary': 'hungary', 'Tortola': 'british-virgin-islands', 'Macedonia': 'macedonia', 'Bonaire': 'bonaire', 'United States': 'united-states', 'Denmark': 'denmark', 'Saba': 'saba', 'Saint John': 'usvirgin-islands', 'Galápagos Islands': 'ecuador', 'Grenada': 'grenada', 'New Caledonia': 'new-caledonia', 'Comoros': 'comoros', 'Cayman Islands': 'cayman-islands', 'Society Islands': 'french-polynesia', 'Uruguay': 'uruguay', 'Canary Islands': 'canary-islands', 'Chad': 'chad', 'Luxembourg': 'luxembourg', 'Eritrea': 'eritrea', 'Scotland': 'united-kingdom', 'Guatemala': 'guatemala', 'Marshall Islands': 'marshall-islands', 'Jamaica': 'jamaica', 'Trinidad and Tobago': 'trinidad-and-tobago', 'Saint Kitts and Nevis': 'st-kitts-and-nevis', 'Barbuda': 'antigua-and-barbuda', 'Thailand': 'thailand', 'Maldives': 'maldives', 'Christmas Island': 'christmas-island', 'Andorra': 'andorra', 'Mauritius': 'mauritius', 'Solomon Islands': 'solomon-islands', 'Azerbaijan': 'azerbaijan', 'Philippines': 'philippines', 'Spain': 'spain', 'Bhutan': 'bhutan', 'Turks and Caicos Islands': 'turks-and-caicos', 'Estonia': 'estonia', 'Sint Eustatius': 'sint-eustatius', 'Bahamas, The': 'the-bahamas', 'Serbia': 'serbia', 'Pitcairn Islands': 'pitcairn-islands', 'Anguilla': 'anguilla', 'Western Sahara': 'western-sahara', 'Gabon': 'gabon', 'Cocos Islands': 'cocos-islands', 'South Africa': 'south-africa', 'Guyana': 'guyana', 'Hong Kong SAR': 'hong-kong-sar', 'Canada': 'canada', 'Tubuai': 'french-polynesia', 'Qatar': 'qatar', 'Nigeria': 'nigeria', 'Ivory Coast': 'ivory-coast', 'Guam': 'guam', 'Fiji': 'fiji', 'Nicaragua': 'nicaragua', 'Guinea': 'guinea', 'Kuwait': 'kuwait', 'British Indian Ocean Territory': 'british-indian-ocean-territory', 'France': 'france', 'Austria': 'austria', 'Kazakhstan': 'kazakhstan', 'Morocco': 'morocco', 'Haiti': 'haiti', 'Tuvalu': 'tuvalu', 'Laos': 'laos', 'Northern Mariana Islands': 'northern-mariana-islands', 'Swaziland': 'swaziland', 'Italy': 'italy', 'Bolivia': 'bolivia', 'Australia': 'australia', 'Albania': 'albania', 'Vietnam': 'vietnam', 'Croatia': 'croatia', 'Papua New Guinea': 'papua-new-guinea', 'Belarus': 'belarus', 'Bangladesh': 'bangladesh', 'Rurutu': 'french-polynesia', 'Togo': 'togo', 'Paraguay': 'paraguay', 'Taiwan': 'taiwan', 'Isle of Man': 'united-kingdom', 'India': 'india', 'Jordan': 'jordan', 'Uzbekistan': 'uzbekistan', 'Tobago': 'trinidad-and-tobago', 'French Polynesia': 'french-polynesia', 'Madeira Islands': 'maderia-islands', 'São Tomé and Príncipe': 'sao-tome-and-principe', 'Portugal': 'portugal', 'Mozambique': 'mozambique', 'Turkey': 'turkey', 'Namibia': 'namibia', 'Russia': 'russia', 'Kenya': 'kenya', 'Israel': 'israel', 'Ecuador': 'ecuador', 'Mongolia': 'mongolia', 'Northern Ireland': 'united-kingdom', 'North Korea': 'north-korea', 'Ghana': 'ghana', 'Cape Verde': 'cape-verde', 'Peru': 'peru', 'Cyprus': 'cyprus', 'Ireland': 'ireland', 'American Samoa': 'american-samoa', 'Niue': 'niue', 'Mayotte': 'mayotte', 'Wales': 'united-kingdom', 'Afghanistan': 'afghanistan', 'Bulgaria': 'bulgaria', 'Honduras': 'honduras', 'Cameroon': 'cameroon', 'Turkmenistan': 'turkmenistan', 'Guernsey': 'united-kingdom', 'Réunion': 'reunion', 'Slovenia': 'slovenia', 'Egypt': 'egypt', 'Burundi': 'burundi', 'Myanmar': 'burma', 'Mali': 'mali', 'Malawi': 'malawi', 'Samoa': 'samoa', 'Virgin Islands, British ': 'british-virgin-islands', 'Greenland': 'greenland', 'Tunisia': 'tunisia', 'Tokelau': 'tokelau', 'Ukraine': 'ukraine', 'Venezuela': 'venezuela', 'Grenadines': 'saint-vincent-and-the-grenadines', 'Zambia': 'zambia', 'Zanzibar': 'tanzania', 'Vatican City': 'italy', 'Germany': 'germany', 'Montserrat': 'montserrat', 'Bahrain': 'bahrain', 'Tahiti': 'french-polynesia', 'Saint Pierre and Miquelon': 'saint-pierre-and-miquelon', 'Indonesia': 'indonesia', 'Tonga': 'tonga', 'Cambodia': 'cambodia', 'Norfolk Island': 'norfolk-island', 'Saipan': 'northern-mariana-islands', 'Iraq': 'iraq', 'Saint Vincent and the Grenadines': 'saint-vincent-and-the-grenadines', 'Brunei': 'brunei'}


def traveler_advice_classes(css_class):
    return css_class == "traveler-disease" or css_class == "traveler-findoutwhy"


def disease_name_and_link(child):
    disease = child.find('a')
    return disease.text, disease.get('href')


def traveler_advice(res):
    """
    Advice data from website
    :param res: requests object gotten from passing traveler tips url to requests.get
    :return: zip object containing health advice for travelers
    """
    website_data = BeautifulSoup(res.text, "html.parser", parse_only=SoupStrainer(class_=traveler_advice_classes))

    website_data_p = [disease_name_and_link(child) for child in website_data.find_all(class_="traveler-disease")]

    website_data_kl = [child.get_text(strip=True) for child in website_data.find_all(class_="traveler-findoutwhy")]

    return zip(website_data_p, website_data_kl)


def serialize_traveler_advice(disease):
    """
    Serialize tips for disease
    :param disease: Contains data for different disease
    :type disease tuple
    :return: Dict where sub-setting with
                name gives the name of disease
                link gives the link to a description of the disease
                tip gives advice for  avoiding that disease
    """
    try:
        disease_management_tip = {"disease_name": disease[0][0], 'disease_link': base_health_tips_url + disease[0][1], 'tip': disease[1]}
        return disease_management_tip
    except IndexError:
        logging.warning("Can not get management tip for {disease}".format(disease=disease))


def get_traveler_health_advice_for_country(country):
    """
    Get health advice for travelers to a country
    :param country: country to get health advice for
    :type country string
    :return: list containing the different advice if any
    """
    try:
        country_query_string = country_dict[country]
    except KeyError:
        logging.error("Ensure country was passed in this format Nigeria or Turks and Caicos Islands or Saint Vincent and the Grenadines")
        return False
    res = requests.get(travel_tips_url_to_query.format(country=country_query_string))
    health_advice = [serialize_traveler_advice(disease) for disease in traveler_advice(res) if disease]
    if health_advice:
        return health_advice
    else:
        logging.error("Could not get health advice for {country}".format(country=country))
        return False


if __name__ == "__main__":
    print(get_traveler_health_advice_for_country('Nigeria'))
