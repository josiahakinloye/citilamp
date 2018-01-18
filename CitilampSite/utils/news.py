"""
Module for anything relating to news
"""
from collections import OrderedDict

import requests

apiKey = 'cf20aa0d287d4f39bbaac6880c56522b'

base_news_url= 'https://newsapi.org/v2/top-headlines?{}&apikey=' + apiKey

country_code_dict = OrderedDict([('Afghanistan', 'af'), ('Albania', 'al'), ('Algeria', 'dz'), ('American Samoa', 'as'), ('Andorra', 'ad'), ('Angola', 'ao'), ('Anguilla', 'ai'), ('Antarctica', 'aq'), ('Antigua and Barbuda', 'ag'), ('Argentina', 'ar'), ('Armenia', 'am'), ('Aruba', 'aw'), ('Australia', 'au'), ('Austria', 'at'), ('Azerbaijan', 'az'), ('Bahamas', 'bs'), ('Bahrain', 'bh'), ('Bangladesh', 'bd'), ('Barbados', 'bb'), ('Belarus', 'by'), ('Belgium', 'be'), ('Belize', 'bz'), ('Benin', 'bj'), ('Bermuda', 'bm'), ('Bhutan', 'bt'), ('Bolivia (Plurinational State of)', 'bo'), ('Bonaire, Sint Eustatius and Saba', 'bq'), ('Bosnia and Herzegovina', 'ba'), ('Botswana', 'bw'), ('Bouvet Island', 'bv'), ('Brazil', 'br'), ('British Indian Ocean Territory', 'io'), ('Brunei Darussalam', 'bn'), ('Bulgaria', 'bg'), ('Burkina Faso', 'bf'), ('Burundi', 'bi'), ('Cabo Verde', 'cv'), ('Cambodia', 'kh'), ('Cameroon', 'cm'), ('Canada', 'ca'), ('Cayman Islands', 'ky'), ('Central African Republic', 'cf'), ('Chad', 'td'), ('Chile', 'cl'), ('China', 'cn'), ('Christmas Island', 'cx'), ('Cocos (Keeling) Islands', 'cc'), ('Colombia', 'co'), ('Comoros', 'km'), ('Congo', 'cg'), ('Congo (Democratic Republic of the)', 'cd'), ('Cook Islands', 'ck'), ('Costa Rica', 'cr'), ('Croatia', 'hr'), ('Cuba', 'cu'), ('Curaçao', 'cw'), ('Cyprus', 'cy'), ('Czech Republic', 'cz'), ("Côte d'Ivoire", 'ci'), ('Denmark', 'dk'), ('Djibouti', 'dj'), ('Dominica', 'dm'), ('Dominican Republic', 'do'), ('Ecuador', 'ec'), ('Egypt', 'eg'), ('El Salvador', 'sv'), ('Equatorial Guinea', 'gq'), ('Eritrea', 'er'), ('Estonia', 'ee'), ('Ethiopia', 'et'), ('Falkland Islands (Malvinas)', 'fk'), ('Faroe Islands', 'fo'), ('Fiji', 'fj'), ('Finland', 'fi'), ('France', 'fr'), ('French Guiana', 'gf'), ('French Polynesia', 'pf'), ('French Southern Territories', 'tf'), ('Gabon', 'ga'), ('Gambia', 'gm'), ('Georgia', 'ge'), ('Germany', 'de'), ('Ghana', 'gh'), ('Gibraltar', 'gi'), ('Greece', 'gr'), ('Greenland', 'gl'), ('Grenada', 'gd'), ('Guadeloupe', 'gp'), ('Guam', 'gu'), ('Guatemala', 'gt'), ('Guernsey', 'gg'), ('Guinea', 'gn'), ('Guinea-Bissau', 'gw'), ('Guyana', 'gy'), ('Haiti', 'ht'), ('Heard Island and McDonald Islands', 'hm'), ('Holy See', 'va'), ('Honduras', 'hn'), ('Hong Kong', 'hk'), ('Hungary', 'hu'), ('Iceland', 'is'), ('India', 'in'), ('Indonesia', 'id'), ('Iran (Islamic Republic of)', 'ir'), ('Iraq', 'iq'), ('Ireland', 'ie'), ('Isle of Man', 'im'), ('Israel', 'il'), ('Italy', 'it'), ('Jamaica', 'jm'), ('Japan', 'jp'), ('Jersey', 'je'), ('Jordan', 'jo'), ('Kazakhstan', 'kz'), ('Kenya', 'ke'), ('Kiribati', 'ki'), ("Korea (Democratic People's Republic of)", 'kp'), ('Korea (Republic of)', 'kr'), ('Kuwait', 'kw'), ('Kyrgyzstan', 'kg'), ("Lao People's Democratic Republic", 'la'), ('Latvia', 'lv'), ('Lebanon', 'lb'), ('Lesotho', 'ls'), ('Liberia', 'lr'), ('Libya', 'ly'), ('Liechtenstein', 'li'), ('Lithuania', 'lt'), ('Luxembourg', 'lu'), ('Macao', 'mo'), ('Macedonia (the former Yugoslav Republic of)', 'mk'), ('Madagascar', 'mg'), ('Malawi', 'mw'), ('Malaysia', 'my'), ('Maldives', 'mv'), ('Mali', 'ml'), ('Malta', 'mt'), ('Marshall Islands', 'mh'), ('Martinique', 'mq'), ('Mauritania', 'mr'), ('Mauritius', 'mu'), ('Mayotte', 'yt'), ('Mexico', 'mx'), ('Micronesia (Federated States of)', 'fm'), ('Moldova (Republic of)', 'md'), ('Monaco', 'mc'), ('Mongolia', 'mn'), ('Montenegro', 'me'), ('Montserrat', 'ms'), ('Morocco', 'ma'), ('Mozambique', 'mz'), ('Myanmar', 'mm'), ('Namibia', 'na'), ('Nauru', 'nr'), ('Nepal', 'np'), ('Netherlands', 'nl'), ('New Caledonia', 'nc'), ('New Zealand', 'nz'), ('Nicaragua', 'ni'), ('Niger', 'ne'), ('Nigeria', 'ng'), ('Niue', 'nu'), ('Norfolk Island', 'nf'), ('Northern Mariana Islands', 'mp'), ('Norway', 'no'), ('Oman', 'om'), ('Pakistan', 'pk'), ('Palau', 'pw'), ('Palestine, State of', 'ps'), ('Panama', 'pa'), ('Papua New Guinea', 'pg'), ('Paraguay', 'py'), ('Peru', 'pe'), ('Philippines', 'ph'), ('Pitcairn', 'pn'), ('Poland', 'pl'), ('Portugal', 'pt'), ('Puerto Rico', 'pr'), ('Qatar', 'qa'), ('Republic of Kosovo', 'xk'), ('Romania', 'ro'), ('Russian Federation', 'ru'), ('Rwanda', 'rw'), ('Réunion', 're'), ('Saint Barthélemy', 'bl'), ('Saint Helena, Ascension and Tristan da Cunha', 'sh'), ('Saint Kitts and Nevis', 'kn'), ('Saint Lucia', 'lc'), ('Saint Martin (French part)', 'mf'), ('Saint Pierre and Miquelon', 'pm'), ('Saint Vincent and the Grenadines', 'vc'), ('Samoa', 'ws'), ('San Marino', 'sm'), ('Sao Tome and Principe', 'st'), ('Saudi Arabia', 'sa'), ('Senegal', 'sn'), ('Serbia', 'rs'), ('Seychelles', 'sc'), ('Sierra Leone', 'sl'), ('Singapore', 'sg'), ('Sint Maarten (Dutch part)', 'sx'), ('Slovakia', 'sk'), ('Slovenia', 'si'), ('Solomon Islands', 'sb'), ('Somalia', 'so'), ('South Africa', 'za'), ('South Georgia and the South Sandwich Islands', 'gs'), ('South Sudan', 'ss'), ('Spain', 'es'), ('Sri Lanka', 'lk'), ('Sudan', 'sd'), ('Suriname', 'sr'), ('Svalbard and Jan Mayen', 'sj'), ('Swaziland', 'sz'), ('Sweden', 'se'), ('Switzerland', 'ch'), ('Syrian Arab Republic', 'sy'), ('Taiwan', 'tw'), ('Tajikistan', 'tj'), ('Tanzania, United Republic of', 'tz'), ('Thailand', 'th'), ('Timor-Leste', 'tl'), ('Togo', 'tg'), ('Tokelau', 'tk'), ('Tonga', 'to'), ('Trinidad and Tobago', 'tt'), ('Tunisia', 'tn'), ('Turkey', 'tr'), ('Turkmenistan', 'tm'), ('Turks and Caicos Islands', 'tc'), ('Tuvalu', 'tv'), ('Uganda', 'ug'), ('Ukraine', 'ua'), ('United Arab Emirates', 'ae'), ('United Kingdom of Great Britain and Northern Ireland', 'gb'), ('United States', 'us'), ('United States Minor Outlying Islands', 'um'), ('Uruguay', 'uy'), ('Uzbekistan', 'uz'), ('Vanuatu', 'vu'), ('Venezuela (Bolivarian Republic of)', 've'), ('Viet Nam', 'vn'), ('Virgin Islands (British)', 'vg'), ('Virgin Islands (U.S.)', 'vi'), ('Wallis and Futuna', 'wf'), ('Western Sahara', 'eh'), ('Yemen', 'ye'), ('Zambia', 'zm'), ('Zimbabwe', 'zw'), ('Åland Islands', 'ax')])

class NewsApiError(Exception):
    """
    Class for handling errors relating to calling the news api
    """
    pass


def get_news_for_country(country):
    try:
        country_code = country_code_dict[country]
    except KeyError:
        print("did not find ")
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