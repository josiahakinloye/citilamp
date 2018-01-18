"""
Module for anything relating to news
"""
import requests
apiKey = 'cf20aa0d287d4f39bbaac6880c56522b'
base_headline_url= 'https://newsapi.org/v2/top-headlines?{}&apikey='+apiKey


class NewsApiError(Exception):
    """
    Class for handling errors relating to calling the news api
    """
    pass


def get_news_for_country(country_code):
    news_for_country_url = base_headline_url.format('country='+country_code)
    response = requests.get(news_for_country_url).json()
    try:
        news = response['articles']
    except KeyError:
        raise NewsApiError("Something went wrong with the news api, could not get news for country with code {}".format(country_code))
    country_news = map(get_some_news_info, news)
    return country_news


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

#simply call this in the front end
def get_headline_news():
    """
    Get headline news from google news
    using google news since it is a news aggregator(so you do not need to get news
    from other sources

    :return: map object that contains 10 headlines
    """
    headline_url = base_headline_url.format('sources=google-news')
    response = requests.get(headline_url).json()
    try:
        headlines = response['articles']
    except:
        raise NewsApiError("Something went wrong with the news api")
    headline_news = map(get_some_news_info, headlines)
    return headline_news

if __name__ == "__main__":
    headline_news = get_headline_news()
    for headline in headline_news:
        print(headline)
        print("\n")
    country_news= get_news_for_country('ng')
    print ("News for country")
    for news in country_news:
        print(news)
        print("\n")