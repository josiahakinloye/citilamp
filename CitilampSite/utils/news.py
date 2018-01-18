"""
Module for anything relating to news
"""
import requests

apiKey = 'cf20aa0d287d4f39bbaac6880c56522b'

base_news_url= 'https://newsapi.org/v2/top-headlines?{}&apikey=' + apiKey

country_code_dict = {'Estonia': 'ee', 'Zambia': 'zm', 'Virgin Islands (British)': 'vg', 'Dominica': 'dm', 'Mongolia': 'mn', 'Turkmenistan': 'tm', 'Solomon Islands': 'sb', 'Nicaragua': 'ni', 'Bouvet Island': 'bv', 'Ireland': 'ie', 'Faroe Islands': 'fo', 'South Georgia and the South Sandwich Islands': 'gs', 'Nauru': 'nr', 'Yemen': 'ye', 'Martinique': 'mq', "Lao People's Democratic Republic": 'la', 'Croatia': 'hr', 'Norfolk Island': 'nf', 'Costa Rica': 'cr', 'Malawi': 'mw', 'Mexico': 'mx', 'Congo (Democratic Republic of the)': 'cd', 'Lebanon': 'lb', 'Bahrain': 'bh', 'Iraq': 'iq', 'Brunei Darussalam': 'bn', 'Kenya': 'ke', 'Uzbekistan': 'uz', 'Gambia': 'gm', 'Zimbabwe': 'zw', 'Macedonia (the former Yugoslav Republic of)': 'mk', 'Guadeloupe': 'gp', 'Angola': 'ao', 'Palestine, State of': 'ps', 'Russian Federation': 'ru', 'Cayman Islands': 'ky', 'Guyana': 'gy', 'Canada': 'ca', 'Mozambique': 'mz', 'Wallis and Futuna': 'wf', 'Malaysia': 'my', 'Madagascar': 'mg', 'Grenada': 'gd', 'Panama': 'pa', 'Uganda': 'ug', 'El Salvador': 'sv', 'Turks and Caicos Islands': 'tc', 'Timor-Leste': 'tl', 'Maldives': 'mv', 'Saint Kitts and Nevis': 'kn', 'Botswana': 'bw', 'Tunisia': 'tn', 'Korea (Republic of)': 'kr', 'Cambodia': 'kh', 'Senegal': 'sn', 'Slovenia': 'si', 'Swaziland': 'sz', 'Dominican Republic': 'do', 'Honduras': 'hn', 'Denmark': 'dk', 'Finland': 'fi', 'United Arab Emirates': 'ae', 'Saint Lucia': 'lc', 'Afghanistan': 'af', 'Guinea': 'gn', 'Ecuador': 'ec', 'Jordan': 'jo', 'Viet Nam': 'vn', 'Germany': 'de', 'Morocco': 'ma', 'Haiti': 'ht', 'Pitcairn': 'pn', 'Ukraine': 'ua', 'Equatorial Guinea': 'gq', 'Namibia': 'na', 'Comoros': 'km', 'Jamaica': 'jm', 'Slovakia': 'sk', 'Sao Tome and Principe': 'st', 'Spain': 'es', 'United Kingdom of Great Britain and Northern Ireland': 'gb', 'Antarctica': 'aq', 'Puerto Rico': 'pr', 'Iran (Islamic Republic of)': 'ir', 'United States Minor Outlying Islands': 'um', 'Bangladesh': 'bd', 'Republic of Kosovo': 'xk', 'Kyrgyzstan': 'kg', 'French Polynesia': 'pf', 'Mauritius': 'mu', 'Lithuania': 'lt', "Korea (Democratic People's Republic of)": 'kp', 'Benin': 'bj', 'Romania': 'ro', 'Liechtenstein': 'li', 'Trinidad and Tobago': 'tt', 'Tuvalu': 'tv', 'Falkland Islands (Malvinas)': 'fk', 'Anguilla': 'ai', 'Ethiopia': 'et', 'Portugal': 'pt', 'Saint Barthélemy': 'bl', 'Egypt': 'eg', 'Northern Mariana Islands': 'mp', 'Hong Kong': 'hk', 'Gibraltar': 'gi', 'Belgium': 'be', 'Togo': 'tg', 'Sudan': 'sd', 'Sierra Leone': 'sl', 'Holy See': 'va', 'Cocos (Keeling) Islands': 'cc', 'Tonga': 'to', 'Sri Lanka': 'lk', 'Syrian Arab Republic': 'sy', 'Micronesia (Federated States of)': 'fm', 'Saint Martin (French part)': 'mf', 'Chile': 'cl', 'Bahamas': 'bs', 'Belize': 'bz', 'Paraguay': 'py', 'Isle of Man': 'im', 'Tokelau': 'tk', 'Bonaire, Sint Eustatius and Saba': 'bq', 'Poland': 'pl', 'New Caledonia': 'nc', 'Taiwan': 'tw', 'Algeria': 'dz', 'Albania': 'al', 'Hungary': 'hu', 'Cyprus': 'cy', 'Greenland': 'gl', 'Malta': 'mt', 'Antigua and Barbuda': 'ag', 'Heard Island and McDonald Islands': 'hm', 'Congo': 'cg', 'Luxembourg': 'lu', 'San Marino': 'sm', 'Indonesia': 'id', 'Barbados': 'bb', 'Georgia': 'ge', 'Iceland': 'is', 'Marshall Islands': 'mh', 'Suriname': 'sr', 'Australia': 'au', 'Italy': 'it', 'Armenia': 'am', 'British Indian Ocean Territory': 'io', 'Christmas Island': 'cx', 'Guam': 'gu', 'Brazil': 'br', 'Eritrea': 'er', 'Åland Islands': 'ax', 'Colombia': 'co', 'Japan': 'jp', 'Oman': 'om', 'Belarus': 'by', 'Liberia': 'lr', 'Bhutan': 'bt', 'Réunion': 're', 'Chad': 'td', 'Tanzania, United Republic of': 'tz', 'Czech Republic': 'cz', 'Curaçao': 'cw', 'Turkey': 'tr', 'Niue': 'nu', 'American Samoa': 'as', 'Saudi Arabia': 'sa', 'Ghana': 'gh', "Côte d'Ivoire": 'ci', 'Lesotho': 'ls', 'Burundi': 'bi', 'United States': 'us', 'Burkina Faso': 'bf', 'Vanuatu': 'vu', 'Bolivia (Plurinational State of)': 'bo', 'Latvia': 'lv', 'Cameroon': 'cm', 'Sweden': 'se', 'South Africa': 'za', 'Papua New Guinea': 'pg', 'Gabon': 'ga', 'Guatemala': 'gt', 'Bosnia and Herzegovina': 'ba', 'Philippines': 'ph', 'Bulgaria': 'bg', 'Svalbard and Jan Mayen': 'sj', 'Venezuela (Bolivarian Republic of)': 've', 'Greece': 'gr', 'Thailand': 'th', 'Jersey': 'je', 'Macao': 'mo', 'Saint Helena, Ascension and Tristan da Cunha': 'sh', 'Monaco': 'mc', 'Saint Vincent and the Grenadines': 'vc', 'Djibouti': 'dj', 'New Zealand': 'nz', 'Guernsey': 'gg', 'Kuwait': 'kw', 'Singapore': 'sg', 'China': 'cn', 'Myanmar': 'mm', 'Montserrat': 'ms', 'Norway': 'no', 'Fiji': 'fj', 'Netherlands': 'nl', 'Israel': 'il', 'Cabo Verde': 'cv', 'Cuba': 'cu', 'France': 'fr', 'Azerbaijan': 'az', 'Moldova (Republic of)': 'md', 'Uruguay': 'uy', 'Rwanda': 'rw', 'Libya': 'ly', 'Guinea-Bissau': 'gw', 'Andorra': 'ad', 'French Guiana': 'gf', 'Samoa': 'ws', 'Switzerland': 'ch', 'Nepal': 'np', 'Tajikistan': 'tj', 'Palau': 'pw', 'Cook Islands': 'ck', 'Saint Pierre and Miquelon': 'pm', 'Western Sahara': 'eh', 'Kazakhstan': 'kz', 'Nigeria': 'ng', 'Somalia': 'so', 'Virgin Islands (U.S.)': 'vi', 'Argentina': 'ar', 'Sint Maarten (Dutch part)': 'sx', 'South Sudan': 'ss', 'Aruba': 'aw', 'Mali': 'ml', 'Mayotte': 'yt', 'French Southern Territories': 'tf', 'Peru': 'pe', 'Montenegro': 'me', 'Mauritania': 'mr', 'Central African Republic': 'cf', 'Serbia': 'rs', 'Bermuda': 'bm', 'Niger': 'ne', 'Pakistan': 'pk', 'Qatar': 'qa', 'Kiribati': 'ki', 'Austria': 'at', 'India': 'in', 'Seychelles': 'sc'}

class NewsApiError(Exception):
    """
    Class for handling errors relating to calling the news api
    """
    pass


def get_news_for_country(country):
    try:
        country_code = country_code_dict[country]
    except KeyError:
        raise Exception("Could not get country code for county {}".format(country))
    news_for_country_url = base_news_url.format('country=' + country_code)
    response = requests.get(news_for_country_url).json()
    try:
        news = response['articles']
    except KeyError:
        raise NewsApiError("Something went wrong with the news api, could not get news for country with code {}".format(country_code))
    country_news = map(get_some_news_info, news)
    return list(country_news)


def get_some_news_info(headline_news):
    """
    This gets some attributes from the payload returned by calling the news_api above
    since the json returns some unneeded keys
    :param headline_news: Dictionary to subset from
    :return: Dictionary of needed keys
    """
    real_news = {}
    real_news['title'] = headline_news['title']
    real_news['description'] = headline_news['description']
    real_news['urlToNewsArticle'] = headline_news['url']
    real_news['urlToImage'] = headline_news['urlToImage']
    return real_news


def get_headline_news():
    """
    Get headline news from google news
    using google news since it is a news aggregator(so you do not need to get news
    from other sources

    :return: map object that contains 10 headlines
    """
    headline_url = base_news_url.format('sources=google-news')
    response = requests.get(headline_url).json()
    try:
        headlines = response['articles']
    except KeyError:
        raise NewsApiError("Something went wrong with the news api")
    headline_news = map(get_some_news_info, headlines)
    return list(headline_news)

if __name__ == "__main__":
    headline_news = get_headline_news()
    for headline in headline_news:
        print(headline)
        print("\n")
    country_news= get_news_for_country('Nigeria')
    print ("News for country")
    for news in country_news:
        print(news)
        print("\n")